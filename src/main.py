from copy_static import copy_dir_recursive
from generate_page import generate_page


def main():
    copy_dir_recursive("static", "public")

    generate_page(
        "content/index.md",
        "template.html",
        "public/index.html"
    )


if __name__ == "__main__":
    main()
