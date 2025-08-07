from ascii_dictionary import ascii_art
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
        lines.append("")  # add a blank row between lines

    return lines


def save_ascii_to_js(text, var_name, file_path, ascii_art, mode='w'):
    lines = text_to_ascii_array(text, ascii_art)
    with open(file_path, mode) as f:
        f.write(f"let {var_name} = [\n")
        for line in lines:
            f.write(f'  "{line}",\n')
        f.write("];\n\n")


# Example usage
save_ascii_to_js("Maulik\nSharma", "pixelText", "ascii_output.js", ascii_art)
save_ascii_to_js("MASTER OF CODE", "pixelTextSmall", "ascii_output.js", ascii_art, mode='a')