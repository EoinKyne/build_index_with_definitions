import csv


def lower_first(line):
    line_dict = {}
    for k, v in line.items():
        line_dict[k.lower()] = v.lower()
    return line_dict


def read_dictionary(path):
    try:
        with open(path, 'r') as f:
            dictionary_reader = csv.DictReader(f)
            words_dict = {}

            for d in dictionary_reader:
                key = d['word'].lower()
                word = d['word']
                word_type = d['wordtype']
                definition = d['definition']
                full_word_description = word + " " + word_type + " " + definition
                full_word_description = full_word_description.strip().replace("\n", "")

                if key in words_dict:
                    words_dict[key] += (full_word_description + '\n\t\t\t\t\t')
                else:
                    words_dict[key] = (full_word_description + "\n\t\t\t\t\t")
    except FileNotFoundError as file_not_found:
        raise file_not_found

    return words_dict
