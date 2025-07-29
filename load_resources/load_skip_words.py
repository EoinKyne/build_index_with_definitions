
def load_skip_words(path):

    try:
        with open(path, 'r') as iw:
            skip_words = iw.read().lower()
    except FileNotFoundError as file_not_found:
        raise file_not_found
    return skip_words

