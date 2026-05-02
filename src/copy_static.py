import os
import shutil


def copy_dir_recursive(src_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    os.mkdir(dest_dir)

    _copy_contents(src_dir, dest_dir)


def _copy_contents(src, dest):
    items = os.listdir(src)

    for item in items:
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)

        else:
            os.mkdir(dest_path)
            _copy_contents(src_path, dest_path)
