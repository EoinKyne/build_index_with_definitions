from pathlib import Path
import os


def print_index_to_console(index):
    for key, val in index.items():
        print(f'Word:\t\t\t {key.title()},  {str(val)}')


def write_index_to_text_file(index):
    name = input("Provide name of book indexed: ")
    extension = 'txt'
    file_name = name + '.' + extension
    current_path = Path.cwd()
    directory = current_path / r"./output"
    file_path = directory / file_name
    with open(file_path, 'w+') as file:
        for key, val in index.items():
            file.write(f'Word:\t\t\t {key.title()},  {str(val)}\n')


def print_word_and_definition_to_console(index):
    word = input("Word to return definition: ").lower()

    if word in index:
        print(f'Word:\t\t\t {word.title()},  {str(index.get(word))}')
