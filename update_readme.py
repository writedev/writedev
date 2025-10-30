import datetime

path = "README.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Determine whether it is day or night
hour = datetime.datetime.utcnow().hour
is_day = 6 <= hour < 18  # between 6 a.m. and 6 p.m. UTC

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
            # We comment or uncomment
            if enable:
                lines[i] = lines[i].replace("<!-- ", "").replace(" -->", "")
            else:
                if not line.strip().startswith("<!--"):
                    lines[i] = f"<!-- {line} -->"
    return "\n".join(lines)

new_content = toggle_section(content, "<!--PART1-->", "<!--PART1_END-->", is_day)
new_content = toggle_section(new_content, "<!--PART2-->", "<!--PART2_END-->", not is_day)

with open(path, "w", encoding="utf-8") as f:
    f.write(new_content)
