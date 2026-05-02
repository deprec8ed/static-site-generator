from copy_static import copy_dir_recursive
from generate_pages import generate_pages_recursive


def main():
    copy_dir_recursive("static", "public")

    generate_pages_recursive(
        "content",
        "template.html",
        "public"
    )


if __name__ == "__main__":
    main()
