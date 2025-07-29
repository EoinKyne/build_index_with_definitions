import pytest

from menu.command_line_menu import select_book_to_build_index, get_library, build_index_from_input


@pytest.fixture
def book_library():
    library = ['resources/books_folder/DeBelloGallico-Caesar.txt', 'resources/books_folder/DivineComedy-Dante.txt',
               'resources/books_folder/HappyPrince-Wilde.txt',
               'resources/books_folder/PictureOfDorianGray-Wilde.txt',
               'resources/books_folder/PoblachtNaHEireann.txt', 'resources/books_folder/ThePrince-Machiavelli.txt',
               'resources/books_folder/WarAndPeace-Tolstoy.txt']
    return library


def test_book_in_library(book_library):
    book = "resources/books_folder/DeBelloGallico-Caesar.txt"
    assert book in book_library


def test_get_library():
    library = get_library()
    assert len(library) == 7


def test_select_book_to_build_index(mocker):
    mocker.patch('builtins.input', return_value="resources/books_folder/DeBelloGallico-Caesar.txt")
    choice = select_book_to_build_index()
    book = "resources/books_folder/DeBelloGallico-Caesar.txt"
    assert book == choice


def test_build_index_from_quit_input():
    with pytest.raises(SystemExit) as exit_info:
        build_index_from_input('q')
    assert exit_info.value.code == 0



