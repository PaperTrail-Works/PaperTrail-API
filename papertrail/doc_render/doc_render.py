from .tectonic import TectonicBind
from .template_render import TemplateRenderer

class DocRender():
    def __init__(self, template_dir: str, tectonic_path: str, tmp_dir='./tmp'):
        self.template_dir: str = template_dir
        self.tectonic_path: str = tectonic_path
        self.tmp_dir: str = tmp_dir

    def render(self, template_file: str, file_name: str, data=dict[str: any]) -> bin:
        trender = TemplateRenderer(template_dir=self.template_dir)
        tex_string = trender.render(template_file=template_file, data=data)

        with open(tex_path := f"{self.tmp_dir}/{file_name}.tex", "w") as f:
            f.write(tex_string)

        tbind = TectonicBind(tectonic_path=self.tectonic_path, output_dir=self.tmp_dir)

        return tbind.render_pdf(tex_path=tex_path)
