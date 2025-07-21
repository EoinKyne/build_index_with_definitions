import csv
import menu.command_line_interface


def lower_first(line):
    line_dict = {}
    for k,v in line.items():
        line_dict[k.lower()] = v.lower()
    return line_dict


def read_dictionary():
    try:
        with open("D:/repositories/python/build_index_of_words_with_definitions/resources/dictionary/dictionary.csv",'r') as f:
            dictionary_reader = csv.DictReader(f)
            dictionary_reader.fieldnames = ['key']
            dictionary_reader.restkey = 'value'
            words_dict = {}

            for d in dictionary_reader:
                key = d['key'].lower()
                value = [s.replace('\n', '') for s in d['value']]
                if key in words_dict:
                    words_dict[key] += [value]
                    # dict_dict[d['key']].extend(d['value'])
                else:
                    words_dict[key] = [value]
    except FileNotFoundError as file_not_found:
        raise file_not_found

    return words_dict



#def read_dictionary():
#    with open("./resources/dictionary/dictionary.csv", 'r') as f:
#        dictionary_reader = csv.DictReader(f)
#        dict_list = []
#        for line in dictionary_reader:
#            line = lower_first(line)
#            dict_list.append(line)
#    return dict_list


#def read_dictionary():
#    record = []
#    word_definition = []
#    word_dictionary = {}
#    word = ''
#    previous_word = ''
#    with open("./resources/dictionary/dictionary.csv", 'r') as f:
#        for line in f:
#            line_lower = line.lower()
#            if line_lower.startswith(" "):
#                complete_definition = complete_definition + line_lower
#            elif line_lower.startswith('\"'):
#                record = line_lower.split(',')
#                word = record[0].replace('\"', "")
#                if word == previous_word:
#                    complete_definition = complete_definition + "\n\t" + line_lower
#                else:
#                    complete_definition = line_lower

#            word_definition.append(complete_definition)

#            previous_word = word
#            word_dictionary[word] = word_definition
#    print("done")
#    return word_dictionary
