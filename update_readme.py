import datetime

path = "README.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

hour = datetime.datetime.utcnow().hour
show_a = hour % 2 == 0

version_a = '<img src="https://raw.githubusercontent.com/writedev/writedev/output/snake.svg" alt="Snake animation" />'
version_b = '''<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/writedev/writedev/output/pacman-contribution-graph-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/writedev/writedev/output/pacman-contribution-graph.svg">
  <img alt="Pac-Man contribution graph" src="https://raw.githubusercontent.com/writedev/writedev/output/pacman-contribution-graph.svg">
</picture>'''

content = content.replace("VERSION_A_PLACEHOLDER", version_a if show_a else "")
content = content.replace("VERSION_B_PLACEHOLDER", version_b if not show_a else "")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
