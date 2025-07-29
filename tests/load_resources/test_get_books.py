import pytest



@pytest.fixture
def book_library():
    library = ['resources/books_folder/DeBelloGallico-Caesar.txt', 'resources/books_folder/DivineComedy-Dante.txt',
               'resources/books_folder/HappyPrince-Wilde.txt',
               'resources/books_folder/PictureOfDorianGray-Wilde.txt',
               'resources/books_folder/PoblachtNaHEireann.txt', 'resources/books_folder/ThePrince-Machiavelli.txt',
               'resources/books_folder/WarAndPeace-Tolstoy.txt']
    return library


