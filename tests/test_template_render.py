from papertrail.doc_render import TemplateRenderer

def test_template_render():

    template_render = TemplateRenderer()
    rendered_doc = template_render.render()

    doc = ""

    assert doc == rendered_doc
