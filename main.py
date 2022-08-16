import os
import traceback

from create import touch, mkdir
from delete import delete_file, delete_directory
from list import dirlist


base = '/home/almaz/PycharmProjects/zeon/zeon_fs/'

commands = {
    'touch': touch,
    'mkdir': mkdir,
    'rm': delete_directory,
    'delete': delete_file,
    'list': dirlist
}

if __name__ == '__main__':
    # shows command options
    print("""
            list - to view. 
                Can use ls for directory to see in current working directory,
            touch - to create a file,
            mkdir - to create a directory,
            delete - to delete a file,
            rm - to delete a directory
            """)

    while True:
        args = input('>>> ').split()
        try:
            command = commands[args[0]]
            if args[1:] is isinstance:
                print(command(base+args[1]))
            print(command(base))

        except:
            print(traceback.print_exc())








"""
My first attempt in doing filesystem
"""
    ## Work with while loop
    # while True:
    #     command = input('> ').lower()
    #
    #     # list option
    #     if command == 'list':
    #         try:
    #             subcommand = '/home/almaz/PycharmProjects/zeon/zeon_fs/' + input('directory >> ')
    #             if subcommand == '/home/almaz/PycharmProjects/zeon/zeon_fs/ls':
    #                 subcommand = 'current'
    #             print(dirlist(subcommand))
    #         except:
    #             print(traceback.print_exc())
    #
    #     # create option
    #     elif command == 'create':
    #         choice = input('Create a file or a directory: ').lower()
    #         if choice == 'directory':
    #             try:
    #                 subcommand = '/home/almaz/PycharmProjects/zeon/zeon_fs/' + input('in directory >> ')
    #                 print(mkdir(subcommand))
    #             except:
    #                 print(traceback.print_exc())
    #
    #         elif choice == 'file':
    #             try:
    #                 subcommand = '/home/almaz/PycharmProjects/zeon/zeon_fs/' + input('in directory >> ')
    #                 print(touch(subcommand))
    #             except:
    #                 print(traceback.print_exc())
    #     elif command == 'delete':
    #         choice = input('Delete a file or a directory: ').lower()
    #         if choice == 'directory':
    #             try:
    #                 subcommand = '/home/almaz/PycharmProjects/zeon/zeon_fs/' + input('path to file or directory >> ')
    #                 print(delete_directory(subcommand))
    #             except:
    #                 print(traceback.print_exc())
    #         elif choice == 'file':
    #             try:
    #                 subcommand = '/home/almaz/PycharmProjects/zeon/zeon_fs/' + input('path to file or directory >> ')
    #                 print(delete_file(subcommand))
    #             except:
    #                 print(traceback.print_exc())
    #     elif command == 'quit':
    #         break
    #
    #     else:
    #         print('There is no such command')