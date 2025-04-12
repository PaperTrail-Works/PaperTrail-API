import re
import subprocess


class TectonicBind:

    def __init__(self, tectonic_path: str, output_dir='./'):
        self.tectonic_path = tectonic_path
        self.output_dir = output_dir

    def render_pdf(self, tex_path:str) -> bin:
        subprocess.run([self.tectonic_path, tex_path, f'--outdir={self.output_dir}'], check=True)

        match = re.match(r".*/([^/]+)$", tex_path)
        filename = match.group(1) if match else tex_path

        pdf_path = self.output_dir + "/" + filename.replace('.tex', '.pdf')

        with open(pdf_path, 'rb') as file:
            file_content = file.read()

        return file_content