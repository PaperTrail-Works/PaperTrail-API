from typing import Any
from jinja2 import Environment, FileSystemLoader


class TemplateRenderer():
    env: Environment

    def __init__(self, template_dir:str):
        self.env = Environment(loader=FileSystemLoader(template_dir))


    def render(self, template_file: str, data: dict[str: Any]) -> str:
        template = self.env.get_template(template_file)
        rendered_text = template.render(**data)
        return rendered_text
