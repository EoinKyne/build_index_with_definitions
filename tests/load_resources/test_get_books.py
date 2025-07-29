from pathlib import WindowsPath
import pytest
from load_resources.get_books import list_books_in_library


def test_get_books_with_invalid_path():
    with pytest.raises(FileNotFoundError):
        list_books_in_library("./invalid/path/")