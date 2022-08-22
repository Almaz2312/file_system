from controller import controller
import sys

"""                                             
python3 main.py add test.txt                    
python3 main.py list                            
python3 main.py delete test.txt                 
"""

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        exit('Need more arguments')

    _, command, *args = sys.argv
    controller(command, *args)
