# Pong Animation Generator

A professional web-based tool for creating customizable Pong-style animations with ASCII text rendering. Generate interactive HTML animations or export as animated GIFs with full control over visual elements, timing, and layout.

## Overview

The Pong Animation Generator converts text into ASCII art and animates it with a classic Pong-style ball-bouncing effect. The tool provides a comprehensive GUI for real-time customization and supports multiple export formats.

## Features

### Text Rendering
- Dual text input system supporting two independent text lines
- Automatic ASCII art conversion using predefined character patterns
- Independent size control for each text line (3-50 pixels)
- Precise X/Y coordinate positioning for layout control

### Visual Customization
- **Text Styling**: Base color, glow effect, and hit-state color configuration
- **Ball Properties**: Adjustable speed (1-10), color, and size (5-30 pixels)
- **Background**: Dual-color animated gradient with configurable animation speed
- **Paddle/Bars**: Customizable color and tracking speed (0.1-1.0)
- **Canvas**: Flexible dimensions (600-2400px width, 400-1200px height)

### Animation Controls
- Real-time preview with live parameter updates
- Ball physics with collision detection
- Smooth paddle tracking with configurable responsiveness
- Wave effects on collision events
- Continuous looping animation

### Export Options
- **HTML Export**: Standalone, self-contained HTML file with embedded animation

## System Requirements

### Prerequisites
- Python 3.7 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)
- 50MB free disk space

### Dependencies
- Flask 2.0+

## Installation

### Step 1: Clone or Download

Download the project files to your local machine:

```bash
cd /path/to/your/directory
```

### Step 2: Install Python Dependencies

Install required packages using pip:

```bash
pip install flask
```

For virtual environment setup (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install flask
```

### Step 3: Verify Installation

Ensure all required files are present:
- `app.py` - Flask backend server
- `index.html` - Frontend GUI interface
- `ascii_dictionary.py` - ASCII character definitions
- `Dynamic_loader_ascii.py` - ASCII conversion logic

## Usage Guide

### Starting the Application

1. Navigate to the project directory:
```bash
cd "PONG Animation"
```

2. Start the Flask server:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

### Creating an Animation

#### Step 1: Configure Text Content
1. Enter your desired text in the "Line 1 (Large Text)" textarea
2. Enter secondary text in the "Line 2 (Small Text)" textarea
3. Use `\n` for multi-line text within each input

#### Step 2: Position and Size
1. Set X/Y coordinates for large text positioning
2. Set X/Y coordinates for small text positioning
3. Adjust "Large Text Size" slider (default: 20px)
4. Adjust "Small Text Size" slider (default: 10px)

#### Step 3: Color Configuration
1. **Text Colors**:
   - Base Color: Primary text color
   - Glow Color: Shadow/glow effect color
   - Hit Color: Color when ball collides with text

2. **Ball Settings**:
   - Speed: Animation velocity (1-10)
   - Color: Ball fill color
   - Size: Ball radius (5-30px)

3. **Background**:
   - Color 1: Primary background color
   - Color 2: Secondary gradient color
   - Animation Speed: Gradient animation rate (1-20)

4. **Paddle/Bar Settings**:
   - Color: Bar fill color
   - Speed: Tracking responsiveness (0.1-1.0)

#### Step 4: Canvas Configuration
1. Set canvas width (600-2400px, default: 1200px)
2. Set canvas height (400-1200px, default: 600px)

#### Step 5: Generate and Preview
1. Click "Generate Animation" button
2. Preview appears in the right panel
3. Make adjustments as needed and regenerate

#### Step 6: Export

**HTML Export**:
1. Click "Download HTML" button
2. Save the standalone HTML file
3. Open the file in any browser for offline viewing

## Technical Details

### Architecture

**Frontend (index.html)**:
- HTML5 Canvas for rendering
- Vanilla JavaScript for animation logic
- CSS3 for responsive GUI layout
- Real-time parameter binding

**Backend (app.py)**:
- Flask REST API endpoints
- ASCII text conversion engine
- Dynamic HTML template generation

### API Endpoints

**GET /**
- Returns the main application interface

**POST /generate**
- Accepts: JSON configuration object
- Returns: ASCII art arrays for both text inputs
- Purpose: Real-time preview generation

**POST /download**
- Accepts: JSON configuration object
- Returns: Standalone HTML file
- Purpose: HTML export functionality

### Configuration Object Schema

```javascript
{
  text1: string,           // Large text content
  text2: string,           // Small text content
  text1X: integer,         // Large text X position
  text1Y: integer,         // Large text Y position
  text1Size: integer,      // Large text size (5-50)
  text2X: integer,         // Small text X position
  text2Y: integer,         // Small text Y position
  text2Size: integer,      // Small text size (3-30)
  textColor: string,       // Hex color code
  glowColor: string,       // Hex color code
  hitColor: string,        // Hex color code
  ballSpeed: float,        // Speed value (1-10)
  ballColor: string,       // Hex color code
  ballSize: integer,       // Radius (5-30)
  bgColor1: string,        // Hex color code
  bgColor2: string,        // Hex color code
  bgSpeed: float,          // Speed value (1-20)
  canvasWidth: integer,    // Width (600-2400)
  canvasHeight: integer,   // Height (400-1200)
  barColor: string,        // Hex color code
  barSpeed: float          // Speed value (0.1-1.0)
}
```

## File Structure

```
PONG Animation/
├── app.py                      # Flask backend server
├── index.html                  # Main GUI interface
├── ascii_dictionary.py         # Character pattern definitions
├── Dynamic_loader_ascii.py     # ASCII conversion utilities
├── ascii_output.js             # Generated ASCII output (auto-created)
├── Dynamic_loader_pong.html    # Legacy standalone version
└── README.md                   # Documentation
```

## Troubleshooting

### Server Won't Start
- Verify Python version: `python --version`
- Check if port 5000 is available
- Ensure Flask is installed: `pip show flask`

### Animation Not Generating
- Check browser console for JavaScript errors
- Verify server is running and accessible
- Ensure text inputs are not empty

### Performance Issues
- Reduce canvas dimensions
- Lower animation speeds
- Close unnecessary browser tabs

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Performance Considerations

- **Canvas Size**: Larger canvases require more processing power
- **Text Size**: Smaller text creates more collision objects
- **Browser Rendering**: Hardware acceleration recommended for smooth animation

## Limitations

- ASCII character set limited to predefined patterns in `ascii_dictionary.py`
- Maximum canvas size: 2400x1200 pixels
- Text positioning requires manual coordinate input

## Future Enhancements

- Visual drag-and-drop text positioning
- Custom ASCII character pattern editor
- Multiple ball support
- Sound effect integration
- Animation timeline controls

## License

This project is provided as-is for educational and commercial use.

## Support

For issues, questions, or feature requests, please refer to the project documentation or contact the development team.

## Version History

**v1.0.0** - Initial release
- Core animation engine
- Dual text support
- HTML export
- Comprehensive GUI controls
