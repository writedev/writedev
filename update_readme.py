import datetime
import re

path = "README.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

hour = datetime.datetime.utcnow().hour
show_a = hour % 2 == 0

def toggle_block(text, tag, enable):
    pattern = rf"<!--{tag}\n(.*?)\n{tag}_END-->"
    def repl(match):
        return match.group(1) if enable else f"<!--{tag}\n{match.group(1)}\n{tag}_END-->"
    return re.sub(pattern, repl, text, flags=re.DOTALL)

content = toggle_block(content, "HOUR_1", show_a)
content = toggle_block(content, "HOUR_2", not show_a)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
