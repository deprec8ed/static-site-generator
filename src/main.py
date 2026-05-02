from copy_static import copy_dir_recursive
from markdown_to_html import markdown_to_html_node


def main():
    copy_dir_recursive("static", "public")


if __name__ == "__main__":
    main()
