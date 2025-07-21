import sys

from output_index import output_index_and_dictionary
from load_resources import get_books, load_dictionary, load_skip_words
from build_index_and_dictionary import build_index_and_dictionary


try:
    word_dictionary = load_dictionary.read_dictionary()
    skip_words = load_skip_words.load_skip_words()
except FileNotFoundError as file_not_found:
    print(file_not_found)
    print("Exiting Error 2")
    sys.exit()


def get_library():
    try:
        books = get_books.list_books_in_library()
        print(books)
    except FileNotFoundError as not_found:
        print(not_found)


def select_book_to_build_index():

    get_library()

    while True:
        print("-" * 20)
        print("\nPlease enter path and book to build index ")
        choice = input(" >> ")
        choice = choice.strip()

        return choice


def build_command_line_interface():

    while True:
        print("\n")
        print("-" * 20)
        print("Build Index and Dictionary interface")
        print("-" * 20)
        print("1 Parse ebook and print to console")
        print("-" * 20)
        print("2 Parse ebook and save to file")
        print("-" * 20)
        print("3 Parse ebook and return a search string by page numbers and definition")
        print("-" * 20)
        print("q Quit and exit")
        print("-" * 20)
        print("Please enter an option from 1 to 4\n")

        choice = input("\n >> ")
        choice = choice.strip()

        if choice == '1':
            try:
                book = select_book_to_build_index()
                index = build_index_and_dictionary.build_index_and_dictionary(book, word_dictionary, skip_words)
                output_index_and_dictionary.print_index_to_console(index)
            except FileNotFoundError as not_found:
                print(not_found)
        elif choice == '2':
            try:
                book = select_book_to_build_index()
                index = build_index_and_dictionary.build_index_and_dictionary(book, word_dictionary, skip_words)
                output_index_and_dictionary.write_index_to_text_file(index)
            except FileNotFoundError as not_found:
                print(not_found)
        elif choice == '3':
            try:
                book = select_book_to_build_index()
                index = build_index_and_dictionary.build_index_and_dictionary(book, word_dictionary, skip_words)
                output_index_and_dictionary.print_word_and_definition_to_console(index)
            except FileNotFoundError as not_found:
                print(not_found)
        elif choice == 'q':
            sys.exit()
        else:
            print("Invalid option")
