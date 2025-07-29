import sys
from unittest.mock import patch
import pytest

from menu.command_line_interface import select_book_to_build_index, get_library, build_index_from_input


@pytest.fixture
def book_library():
    library = ['resources/books_folder/DeBelloGallico-Caesar.txt', 'resources/books_folder/DivineComedy-Dante.txt',
               'resources/books_folder/HappyPrince-Wilde.txt',
               'resources/books_folder/PictureOfDorianGray-Wilde.txt',
               'resources/books_folder/PoblachtNaHEireann.txt', 'resources/books_folder/ThePrince-Machiavelli.txt',
               'resources/books_folder/WarAndPeace-Tolstoy.txt']
    return library


@pytest.fixture()
def choose_book():
    book = "resources/books_folder/DeBelloGallico-Caesar.txt"
    return book


def test_book_in_library(book_library):
    book = "resources/books_folder/DeBelloGallico-Caesar.txt"
    print(book)
    assert book in book_library


def test_get_library():
    library = get_library()
    print(type(library))
    assert len(library) == 7


def test_select_book_to_build_index(mocker):
    mocker.patch('builtins.input', return_value="resources/books_folder/DeBelloGallico-Caesar.txt")
    choice = select_book_to_build_index()
    book = "resources/books_folder/DeBelloGallico-Caesar.txt"
    assert book == choice


#def test_build_command_line_interface_calls_build_index_from_input(mocker):
#    mocker.patch('builtins.input', return_value="resources/books_folder/DeBelloGallico-Caesar.txt")
#    with patch('select_book_to_build_index') as mk:
#        build_index_from_input('1')
#        mk.assert_called_once()
#    select_book_to_build_index()
# mocker.assert_has_calls([mocker.call(select_book_to_build_index())])
# select_book_to_build_index().assert_call
#    assert 0


def test_build_index_from_quit_input():
    with pytest.raises(SystemExit) as exit_info:
        build_index_from_input('q')
    assert exit_info.value.code == 0


#def test_build_index_from_invalid_input(mocker):
#    choice = mocker.patch('builtins.input', return_value='q')
#    mock_print = mocker.patch('builtins.print')
#    build_index_from_input('r')
#    mock_print.assert_called_once_with("Invalid option")
#    print(mock_print == "Invalid option")
#    if choice == 'q':
#        sys.exit()
