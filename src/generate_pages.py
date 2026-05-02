import os
from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively walks content directory and generates HTML files
    preserving folder structure inside public/
    """

    items = os.listdir(dir_path_content)

    for item in items:
        src_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(src_path):
            if src_path.endswith(".md"):
                dest_path = dest_path.replace(".md", ".html")

                print(f"Generating page: {src_path} → {dest_path}")

                generate_page(src_path, template_path, dest_path)

        else:
            generate_pages_recursive(src_path, template_path, dest_path)
