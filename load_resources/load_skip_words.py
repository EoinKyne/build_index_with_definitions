import menu.command_line_interface


def load_skip_words():

    try:
        with open("./resources/ignore_words/IgnoreWords.txt", 'r') as iw:
            skip_words = iw.read().lower()
    except FileNotFoundError as file_not_found:
        raise file_not_found
    return skip_words

