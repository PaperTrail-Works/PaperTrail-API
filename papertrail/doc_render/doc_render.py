from typing import Any
from pydantic.v1 import BaseModel, Field


class DocRender(BaseModel):
    template_dir: str = Field(title="", description="")
    template_file: str = Field(title="", description="")
    data: dict[str: Any] = Field(title="", description="")
    tectonic_bin: str = Field(title="", description="")


    def __init__(self, **data: Any):
        super().__init__(**data)
        ...