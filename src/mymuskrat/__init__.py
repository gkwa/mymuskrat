import sys

from . import main2


def main() -> int:
    template_content = main2.load_template("main.go.j2")
    out = main2.render_template(template_content)
    sys.stdout.write(out)
    return 0
