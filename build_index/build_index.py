import re

from word import Word


def build_index_and_dictionary(file, word_dictionary, skip_words):
    book_index_and_dictionary = {}

    line_counter = 0
    page_counter = 1
    text_line = []

    try:
        with open(file) as book:
            for line in book:
                line_counter += 1
                if line_counter % 40 == 0:
                    page_counter += 1

                text_line = re.sub(r'[^a-zA-Z]', " ", line).lower().split(' ')

                for wd in text_line:
                    if wd in skip_words:
                        continue

                    if wd in book_index_and_dictionary:
                        book_index_and_dictionary[wd].set_indices(page_counter)
                    else:
                        if wd in word_dictionary:
                            new_word = Word('', set())
                            new_word.set_definition(word_dictionary.get(wd))
                            new_word.set_indices(page_counter)
                            book_index_and_dictionary[wd] = new_word
                        else:
                            new_word = Word('', set())
                            new_word.set_definition('[ Undefined ]')
                            new_word.set_indices(page_counter)
                            book_index_and_dictionary[wd] = new_word
    except FileNotFoundError as file_not_found:
        raise file_not_found

    return dict(sorted(book_index_and_dictionary.items()))
