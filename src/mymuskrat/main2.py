import pathlib
from jinja2 import Environment, PackageLoader, select_autoescape

import jinja2

TEMPLATES_DIR = "templates"



def load_template(template_name):
    TEMPLATES_PATH = pathlib.Path(__file__).resolve().parent / TEMPLATES_DIR
    path = TEMPLATES_PATH / template_name
    print(f"Loading template from {path}")
    with open(path, "r") as file:
        return file.read()


def render_template(template_content):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIR))


    env = Environment(
        loader=PackageLoader("mymuskrat"),
        autoescape=select_autoescape()
    )

    template = env.from_string(template_content)
    return template.render()
