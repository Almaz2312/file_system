import os
from pathlib import Path


def dirlist(*args):
    print(*os.listdir(Path(__file__).parent / 'fs'), sep=' (^@^) ')
