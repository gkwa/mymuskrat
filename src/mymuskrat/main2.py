import pathlib

import jinja2

TEMPLATES_DIR = "templates"

def load_template(template_name):
    TEMPLATES_PATH = pathlib.Path(__file__).resolve().parent / TEMPLATES_DIR
    path = TEMPLATES_PATH / template_name
    print(f"Loading template from {path}")
    with open(path, "r") as file:
        return file.read()

def render_template(template_content):
    print(f"__file__: {__file__}")
    print(f"__name__: {__name__}")
    package_name = __name__.split(".")[0]
    print(f"package_name: {package_name}")
    loader = jinja2.PackageLoader(package_name, package_path=TEMPLATES_DIR)
    env = jinja2.Environment(loader=loader)

    template = env.from_string(template_content)
    return template.render()
