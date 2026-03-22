from flask import Flask, request, jsonify, send_file
from ascii_dictionary import ascii_art
import io

app = Flask(__name__)

def text_to_ascii_array(text, ascii_art):
    lines = []
    text_lines = text.upper().split("\n")
    
    for line in text_lines:
        output_lines = [""] * 5
        for ch in line:
            pattern = ascii_art.get(ch, ["     "] * 5)
            for i in range(5):
                output_lines[i] += pattern[i] + " "
        lines.extend(output_lines)
        lines.append("")
    
    return lines

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    config = request.json
    
    ascii_large = text_to_ascii_array(config['text1'], ascii_art)
    ascii_small = text_to_ascii_array(config['text2'], ascii_art)
    
    return jsonify({
        'success': True,
        'ascii': {
            'pixelText': ascii_large,
            'pixelTextSmall': ascii_small
        }
    })

@app.route('/download', methods=['POST'])
def download():
    config = request.json
    
    ascii_large = text_to_ascii_array(config['text1'], ascii_art)
    ascii_small = text_to_ascii_array(config['text2'], ascii_art)
    
    html_content = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Pong Animation</title>
  <style>
    body {{ margin: 0; background: black; overflow: hidden; display: flex; justify-content: center; align-items: center; height: 100vh; }}
    canvas {{ display: block; background-color: {config['bgColor1']}; }}
  </style>
</head>
<body>
  <canvas id="gameCanvas"></canvas>
  <script>
    const pixelText = {ascii_large};
    const pixelTextSmall = {ascii_small};
    
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    
    canvas.width = {config['canvasWidth']};
    canvas.height = {config['canvasHeight']};
    
    const gridSize = {config['text1Size']};
    const smallGridSize = {config['text2Size']};
    const chars = [];
    const waves = [];
    
    pixelText.forEach((line, row) => {{
      line.split('').forEach((char, col) => {{
        if (char === '#') {{
          chars.push({{
            x: {config['text1X']} + col * gridSize,
            y: {config['text1Y']} + row * gridSize,
            size: gridSize,
            hit: false
          }});
        }}
      }});
    }});
    
    pixelTextSmall.forEach((line, row) => {{
      line.split('').forEach((char, col) => {{
        if (char === '#') {{
          chars.push({{
            x: {config['text2X']} + col * smallGridSize,
            y: {config['text2Y']} + row * smallGridSize,
            size: smallGridSize,
            hit: false
          }});
        }}
      }});
    }});
    
    let ball = {{
      x: canvas.width / 2,
      y: canvas.height / 2,
      dx: {config['ballSpeed']},
      dy: {config['ballSpeed']} * 0.7,
      radius: {config['ballSize']}
    }};
    
    const platforms = [
      {{ x: 0, y: 100, width: 15, height: 200, axis: 'y' }},
      {{ x: canvas.width - 15, y: 100, width: 15, height: 200, axis: 'y' }},
      {{ x: 400, y: 0, width: 200, height: 15, axis: 'x' }},
      {{ x: 400, y: canvas.height - 15, width: 200, height: 15, axis: 'x' }}
    ];
    
    function updateBall() {{
      ball.x += ball.dx;
      ball.y += ball.dy;
      
      if (ball.x <= 0 || ball.x >= canvas.width) ball.dx *= -1;
      if (ball.y <= 0 || ball.y >= canvas.height) ball.dy *= -1;
      
      for (let i = 0; i < chars.length; i++) {{
        const c = chars[i];
        if (c.hit) continue;
        const dx = Math.abs(ball.x - c.x);
        const dy = Math.abs(ball.y - c.y);
        if (dx < ball.radius + c.size / 2 && dy < ball.radius + c.size / 2) {{
          c.hit = true;
          waves.push({{ x: ball.x, y: ball.y, radius: 0, alpha: 1 }});
          if (dx > dy) ball.dx *= -1;
          else ball.dy *= -1;
          break;
        }}
      }}
      
      platforms.forEach((p) => {{
        if (ball.x + ball.radius > p.x && ball.x - ball.radius < p.x + p.width &&
            ball.y + ball.radius > p.y && ball.y - ball.radius < p.y + p.height) {{
          waves.push({{ x: ball.x, y: ball.y, radius: 0, alpha: 1 }});
          if (p.axis === 'y') ball.dx *= -1;
          else ball.dy *= -1;
        }}
      }});
    }}
    
    function movePlatforms() {{
      platforms.forEach((p) => {{
        const target = p.axis === 'y' ? ball.y - p.height / 2 : ball.x - p.width / 2;
        if (p.axis === 'y') {{
          p.y += (target - p.y) * {config['barSpeed']};
          p.y = Math.max(0, Math.min(canvas.height - p.height, p.y));
        }} else {{
          p.x += (target - p.x) * {config['barSpeed']};
          p.x = Math.max(0, Math.min(canvas.width - p.width, p.x));
        }}
      }});
    }}
    
    function drawWaves() {{
      for (let i = waves.length - 1; i >= 0; i--) {{
        const w = waves[i];
        ctx.beginPath();
        ctx.arc(w.x, w.y, w.radius, 0, Math.PI * 2);
        ctx.strokeStyle = `rgba(255,255,255,${{w.alpha}})`;
        ctx.lineWidth = 2;
        ctx.stroke();
        w.radius += 2;
        w.alpha -= 0.02;
        if (w.alpha <= 0) waves.splice(i, 1);
      }}
    }}
    
    function hexToRgb(hex) {{
      const result = /^#?([a-f\\d]{{2}})([a-f\\d]{{2}})([a-f\\d]{{2}})$/i.exec(hex);
      return result ? {{
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
      }} : {{ r: 0, g: 0, b: 0 }};
    }}
    
    function interpolateColor(color1, color2, factor) {{
      const c1 = hexToRgb(color1);
      const c2 = hexToRgb(color2);
      const r = Math.round(c1.r + (c2.r - c1.r) * factor);
      const g = Math.round(c1.g + (c2.g - c1.g) * factor);
      const b = Math.round(c1.b + (c2.b - c1.b) * factor);
      return `rgb(${{r}},${{g}},${{b}})`;
    }}
    
    function draw() {{
      const gradSize = 40;
      for (let y = 0; y < canvas.height; y += gradSize) {{
        for (let x = 0; x < canvas.width; x += gradSize) {{
          const brightness = 20 + Math.floor(10 * Math.sin((x + y + Date.now() / {config['bgSpeed']}) * 0.01));
          const color = interpolateColor('{config['bgColor1']}', '{config['bgColor2']}', brightness / 40);
          ctx.fillStyle = color;
          ctx.fillRect(x, y, gradSize, gradSize);
        }}
      }}
      
      drawWaves();
      
      chars.forEach((c) => {{
        ctx.fillStyle = c.hit ? '{config['hitColor']}' : '{config['textColor']}';
        ctx.shadowColor = c.hit ? '{config['hitColor']}' : '{config['glowColor']}';
        ctx.shadowBlur = 10;
        ctx.fillRect(c.x - c.size / 2, c.y - c.size / 2, c.size, c.size);
        ctx.shadowBlur = 0;
      }});
      
      ctx.fillStyle = '{config['ballColor']}';
      ctx.beginPath();
      ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
      ctx.fill();
      
      ctx.fillStyle = '{config['barColor']}';
      platforms.forEach((p) => {{
        ctx.fillRect(p.x, p.y, p.width, p.height);
      }});
    }}
    
    function animate() {{
      requestAnimationFrame(animate);
      updateBall();
      movePlatforms();
      draw();
    }}
    
    animate();
  </script>
</body>
</html>'''
    
    return send_file(
        io.BytesIO(html_content.encode('utf-8')),
        mimetype='text/html',
        as_attachment=True,
        download_name='pong_animation.html'
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
