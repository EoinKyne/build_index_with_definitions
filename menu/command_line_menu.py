import sys

from output_index import output_index
from load_resources import get_books, load_dictionary, load_skip_words
from build_index import build_index

# paths
skip_words_path = "./resources/ignore_words/IgnoreWords.txt"
dictionary_path = "D:/repositories/python/build_index_of_words_with_definitions/resources/dictionary/dictionary.csv"
library_path = "./resources/books_folder/"

try:
    word_dictionary = load_dictionary.read_dictionary(dictionary_path)
    skip_words = load_skip_words.load_skip_words(skip_words_path)
except FileNotFoundError as file_not_found:
    print(file_not_found)
    print("Exiting Error 2")
    sys.exit()


def get_titles():
    return f'Word:\t\t\t\tDetails:\n'


def get_library():
    books = []
    try:
        books = get_books.list_books_in_library(library_path)
    except FileNotFoundError as not_found:
        print(not_found)
    return books


def select_book_to_build_index():

    books = get_library()
    print(books)

    while True:
        print("-" * 20)
        print("\nPlease enter path and book to build index ")
        choice = input(" >> ")
        choice = choice.strip()

        return choice


def build_index_from_input(choice):
    if choice == '1':
        try:
            book = select_book_to_build_index()
            index = build_index.build_index(book, word_dictionary, skip_words)
            output_index.print_index_to_console(index)
        except FileNotFoundError as not_found:
            print(not_found)
    elif choice == '2':
        try:
            book = select_book_to_build_index()
            index = build_index.build_index(book, word_dictionary, skip_words)
            output_index.write_index_to_text_file(index)
        except FileNotFoundError as not_found:
            print(not_found)
    elif choice == '3':
        try:
            book = select_book_to_build_index()
            index = build_index.build_index(book, word_dictionary, skip_words)
            output_index.print_word_and_definition_to_console(index)
        except FileNotFoundError as not_found:
            print(not_found)
    elif choice == 'q':
        sys.exit(0)
    else:
        print("Invalid option")

    build_command_line_interface()


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
        print("Please enter an option from 1 to 3 or q to quit\n")

        choice = input(" >> ")
        choice = choice.strip()
        print(choice)
        return build_index_from_input(choice)


