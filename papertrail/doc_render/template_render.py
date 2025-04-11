from typing import Any
from jinja2 import Environment, FileSystemLoader
from pydantic.v1 import BaseModel, Field


class TemplateRenderer(BaseModel):
    template_dir: str = Field(title="", description="")

    def __init__(self):
        super().__init__()

        env = Environment(loader=FileSystemLoader(self.template_dir))
        self.template = env.get_template(self.template_file)

    def render(self, template_file: str, data: dict[str: Any]) -> str:
        rendered_text = self.template.render(name="World")
        return rendered_text
