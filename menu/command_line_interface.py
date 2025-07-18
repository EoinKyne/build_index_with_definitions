import sys

import output_index_and_dictionary
from book_repository import get_books
from build_index_and_dictionary import build_index_and_dictionary
from datetime import datetime


def select_book_to_build_index():

    while True:
        print("-" * 20)
        print("\nPlease enter path and book to build index ")
        choice = input(" >> ")
        choice = choice.strip()

        return choice


def build_command_line_interface():

    while True:
        print("\n-" * 20)
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
            start = datetime.now()
            book = ''
            try:
                books = get_books.list_books_in_library()
                print(books)
                book = select_book_to_build_index()
            except FileNotFoundError as file_not_found:
                print(file_not_found)

            index = build_index_and_dictionary.build_index_and_dictionary(book)
            output_index_and_dictionary.print_index_to_console(index)
            end = datetime.now()
            print(end - start)
        elif choice == '2':
            book = ''
            try:
                books = get_books.list_books_in_library()
                print(books)
                book = select_book_to_build_index()
            except FileNotFoundError as file_not_found:
                print(file_not_found)

            index = build_index_and_dictionary.build_index_and_dictionary(book)

        elif choice == '3':
            print('3')
        elif choice == 'q':
            sys.exit()
        else:
            print("Invalid option")
