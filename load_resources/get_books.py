import glob
import pathlib


def list_books_in_library(directory):
    files = []
    try:
        files = [f for f in pathlib.Path(directory).iterdir() if f.is_file() and f.suffix.lower() == '.txt']
    except FileNotFoundError as file_not_found:
        print(file_not_found, "\n")
        raise file_not_found
    return files

