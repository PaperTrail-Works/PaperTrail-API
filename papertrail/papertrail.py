from doc_render import DocRender
from pathlib import Path

folder = Path("tmp")
folder.mkdir(parents=True, exist_ok=True)

doc_render = DocRender(
    template_dir='docs/jinja',
    tectonic_path='bin/tectonic',
    tmp_dir='tmp'
    )

pdf_content = doc_render.render(
    template_file='hello.jinja2',
    file_name='example',
    data={'name': 'World'}
)

with open('./example_resume.pdf', 'wb') as f:
    f.write(pdf_content)