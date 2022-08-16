import os
import traceback

from create import touch, mkdir
from delete import delete_file, delete_directory
from list import dirlist


if __name__ == '__main__':
    print("""
            list - to view. 
                Can use ls for directory to see in current working directory,
            create - to create directory or a file,
            delete - to delete directory or a file
            """)
    while True:
        command = input('> ').lower()

        if command == 'list':
            try:
                subcommand = '/home/almaz/PycharmProjects/zeon/zeon_fs/' + input('directory >> ')
                if subcommand == '/home/almaz/PycharmProjects/zeon/zeon_fs/ls':
                    subcommand = 'current'
                print(dirlist(subcommand))
            except:
                print(traceback.print_exc())

        elif command == 'create':
            choice = input('Create a file or a directory: ').lower()
            if choice == 'directory':
                try:
                    subcommand = '/home/almaz/PycharmProjects/zeon/zeon_fs/' + input('in directory >> ')
                    print(mkdir(subcommand))
                except:
                    print(traceback.print_exc())

            elif choice == 'file':
                try:
                    subcommand = '/home/almaz/PycharmProjects/zeon/zeon_fs/' + input('in directory >> ')
                    print(touch(subcommand))
                except:
                    print(traceback.print_exc())
        elif command == 'delete':
            choice = input('Delete a file or a directory: ').lower()
            if choice == 'directory':
                try:
                    subcommand = '/home/almaz/PycharmProjects/zeon/zeon_fs/' + input('path to file or directory >> ')
                    print(delete_directory(subcommand))
                except:
                    print(traceback.print_exc())
            elif choice == 'file':
                try:
                    subcommand = '/home/almaz/PycharmProjects/zeon/zeon_fs/' + input('path to file or directory >> ')
                    print(delete_file(subcommand))
                except:
                    print(traceback.print_exc())
        elif command == 'quit':
            break

        else:
            print('There is no such command')
