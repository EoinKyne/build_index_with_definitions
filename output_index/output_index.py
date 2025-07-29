from pathlib import Path


def get_titles():
    return f'Word:\t\t\t\tDetails:\n'


def print_index_to_console(index):
    print(get_titles())
    for key, val in index.items():
        print(f'{key.title()}\t\t\t\t {str(val)}')


def write_index_to_text_file(index):
    name = input("Provide name of index to be saved : ").split('.', 1)[0]
    extension = 'txt'
    file_name = name + '.' + extension
    current_path = Path.cwd()
    directory = current_path / r"./output"
    file_path = directory / file_name
    try:
        with open(file_path, 'w+') as file:
            file.write(get_titles())
            for key, val in index.items():
                file.write(f'{key.title()}\t\t\t\t{str(val)}')
    except FileNotFoundError as file_not_found:
        raise file_not_found


def print_word_and_definition_to_console(index):
    word = input("Word to return definition: ").lower()
    print(get_titles())
    print(f'{word.title()}\t\t\t\t {str(index.get(word))}')

