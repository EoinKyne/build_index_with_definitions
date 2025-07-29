import os
import sys

import menu.command_line_menu
from menu import command_line_menu


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        menu.command_line_menu.build_command_line_interface()
    except KeyboardInterrupt:
        print('\nInterrupted')
        try:
            sys.exit()
        except SystemExit as se:
            print(se)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
