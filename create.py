from pathlib import Path

from fs_db import add_to_name_db, add_to_content_db


def add(root, file_path):


    add_to_name_db(root, file_path)
    add_to_content_db(root, file_path)
