import pathlib
from pathlib import Path
import os

from create import add
from delete import delete_file
from list import dirlist


root = Path(__file__).parent / '.fs'

if not pathlib.Path(root).exists():
    os.mkdir(root)

# storage_path = root /

commands = {
    'add': add,
    'delete': delete_file,
    'list': dirlist,
    # 'add_h': hash_dir
}


def controller(command, *args):

    if command not in commands:
        exit('Not in commands')

    commands[command](root, *args)  # type: ignore
