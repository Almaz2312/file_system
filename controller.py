import pathlib
from pathlib import Path
import os
import sys

from create import add, mkdir
from delete import delete_file, delete_directory
from list import dirlist


root = Path(__file__).parent / 'fs'
if not pathlib.Path(root).exists():
    os.mkdir(root)

commands = {
    'add': add,
    'mkdir': mkdir,
    'rm': delete_directory,
    'delete': delete_file,
    'list': dirlist
}


def controller():
    if len(sys.argv) <= 1:
        exit('Need more arguments')

    _, command, *args = sys.argv

    if command not in commands:
        exit('Not in commands')

    if command == 'list':
        commands[command]()  # type: ignore
    else:
        commands[command](root, *args)  # type: ignore
