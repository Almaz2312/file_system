import os
from pathlib import Path


def dirlist(*args):

    _ = args
    files = os.scandir(Path(__file__).parent / 'fs')

    for file in files:
        print(file.name, os.path.getsize(file), sep='\t')
