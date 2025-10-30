import datetime

# Path to README
path = "README.md"

# Read the current content
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Determine which version to show (alternating every hour)
hour = datetime.datetime.utcnow().hour
show_a = hour % 2 == 0  # Even hours -> A, Odd hours -> B

def toggle_section(text, start_tag, end_tag, enable):
    lines = text.split("\n")
    inside = False
    for i, line in enumerate(lines):
        if start_tag in line:
            inside = True
            continue
        if end_tag in line:
            inside = False
            continue
        if inside:
            if enable:
                lines[i] = lines[i].replace("<!-- ", "").replace(" -->", "")
            else:
                if not line.strip().startswith("<!--"):
                    lines[i] = f"<!-- {line} -->"
    return "\n".join(lines)

# Toggle sections
new_content = toggle_section(content, "<!--HOUR_1-->", "<!--HOUR_1_END-->", show_a)
new_content = toggle_section(new_content, "<!--HOUR_2-->", "<!--HOUR_2_END-->", not show_a)

# Write back updated README
with open(path, "w", encoding="utf-8") as f:
    f.write(new_content)
