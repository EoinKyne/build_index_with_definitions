from pathlib import Path
import re

from build_index_and_dictionary.word import Word
from load_dictionary import load_dictionary
from load_skip_words import load_skip_words


def build_index_and_dictionary(file):
    word_dictionary = []
    word_dictionary = load_dictionary.read_dictionary()
    skip_words = load_skip_words.load_skip_words()
    book_index_and_dictionary = {}
    # get all the key (word) in list of dictionaries
    #list_of_keys = [d.get('word') for d in word_dictionary if 'word' in d]

    line_counter = 0
    page_counter = 1
    text_line = []

    with open(file) as book:

        for line in book:
            line_counter += 1
            if line_counter % 40 == 0:
                page_counter += 1

            text_line = re.sub(r'[^a-zA-z]', " ", line).lower().split(' ')

            for wd in text_line:
                if wd in skip_words:
                    continue

                if wd in book_index_and_dictionary:
                    book_index_and_dictionary[wd].set_indices(page_counter)
                else:
                    if wd in word_dictionary:
                        # get the index of the word in the list of dictionaries
                    #    ind = list_of_keys.index(wd)
                    #    dictionary_item = word_dictionary[ind]
                        new_word = Word('', [])
                        #new_word.set_word_type(dictionary_item.get('wordtype'))
                        new_word.set_definition(word_dictionary.get(wd))
                        new_word.set_indices(page_counter)
                        book_index_and_dictionary[wd] = new_word
                    else:
                        new_word = Word('', [])
                        #new_word.set_word_type(' ')
                        new_word.set_definition('Undefined')
                        new_word.set_indices(page_counter)
                        book_index_and_dictionary[wd] = new_word

    return book_index_and_dictionary
        #for key, val in book_index_and_dictionary.items():
            #print(f'Word: {key},  {str(val)}')
