import os
import sys
import pathlib
from pathlib import Path

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
"""
python3 main.py add test.txt
python3 main.py list
python3 main.py delete test.txt
"""


if len(sys.argv) <= 1:
    exit('Need more arguments')

_, command, *args = sys.argv


if command not in commands:
    exit('Not in commands')

commands[command](root, *args)