import unittest
from papertrail.doc_render import TemplateRenderer, TectonicBind


class TestRenderers(unittest.TestCase):

    def test_template_render(self):
        template_render = TemplateRenderer(template_dir='./test_data/jinja')
        rendered_string = template_render.render(template_file='hello.jinja2', data={'name': 'world'})

        data_str = "Hello, world!"

        assert data_str == rendered_string


    def test_pdf_render(self):
        tectonic = TectonicBind(tectonic_path='../papertrail/bin/tectonic')
        file_content = tectonic.render_pdf('./test_data/tex/hello.tex')

        with open('./test_data/pdf/hello.pdf', 'rb') as file:
            cmp_file = file.read()

        assert cmp_file == file_content

