# -*- coding: utf-8 -*-
"""Build Jinja sources"""
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, Template, select_autoescape

TEMPLATES: list[Path] = [
    Path("index.html")
]
OUTPUT: Path = Path("output")

env: Environment = Environment(
    loader=FileSystemLoader(Path("src/html/")),
    autoescape=select_autoescape()
)

for template in TEMPLATES:
    print(f"Building {template}")

    template_object: Template = env.get_template(str(template))
    output: str = template_object.render()

    with open(OUTPUT / template, "w", encoding="utf-8") as file:
        file.write(output)
