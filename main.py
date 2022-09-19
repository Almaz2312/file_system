import sys

from create import add
from delete import delete_file
from list import dirlist

"""                                             
python3 main.py add test.txt                    
python3 main.py list                            
python3 main.py delete test.txt                 
"""

commands = {
    'add': add,
    'delete': delete_file,
    'list': dirlist
}

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        exit('Need more arguments')

    _, command, *args = sys.argv
    if command not in commands:
        print("unknown command")
        exit()

    commands[command](args)
