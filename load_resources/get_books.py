import os
import sys
from pathlib import Path
import menu.command_line_interface


def list_books_in_library():
    files = []
    try:
        directory = Path("./resources/books_folder/")
        files = [f for f in directory.iterdir() if f.is_file()]
    except FileNotFoundError as file_not_found:
        print(file_not_found, "\n")
        raise file_not_found
    return files

