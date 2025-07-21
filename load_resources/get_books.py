import os
from pathlib import Path


def list_books_in_library():
    directory = Path("./resources/books_folder/")
    files = [f for f in directory.iterdir() if f.is_file()]
    return files

