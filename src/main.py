import sys

from copy_static import copy_dir_recursive
from generate_pages import generate_pages_recursive


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    output_dir = "docs"

    copy_dir_recursive("static", output_dir)

    generate_pages_recursive(
        "content",
        "template.html",
        output_dir,
        basepath
    )


if __name__ == "__main__":
    main()
