import pathlib

import jinja2

TEMPLATES_DIR = "templates"


def load_template(template_name):
    TEMPLATES_PATH = pathlib.Path(__file__).resolve().parent / TEMPLATES_DIR
    path = TEMPLATES_PATH / template_name
    with open(path, "r") as file:
        return file.read()


def render_template(template_content):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIR))
    template = env.from_string(template_content)
    return template.render()
