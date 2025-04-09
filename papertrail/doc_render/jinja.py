from jinja2 import Environment, FileSystemLoader

# -- Config --
TEMPLATE_DIR = "templates"  # Folder where template.txt is stored
TEMPLATE_FILE = "template.txt"  # Name of the template file

# -- Jinja Environment Setup --
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(TEMPLATE_FILE)

# -- Render the template with a name variable --
rendered_text = template.render(name="World")

# -- Print the rendered text (you can save it or print) --
print(rendered_text)
