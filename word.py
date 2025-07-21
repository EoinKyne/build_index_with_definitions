class Word:

    def __init__(self, definition, indices):
        self.__definition = definition
        self.__indices = indices

    def get_definition(self):
        return self.__definition

    def set_definition(self, definition):
        self.__definition = definition

    def get_indices(self):
        return self.__indices

    def set_indices(self, indices):
        self.__indices.append(indices)

    def __str__(self):
        #return '\nDefinition: ' + str(self.__definition).join('], [') + '\nPages: ' + str(self.__indices) + '\n'
        #return '\nDefinitions:\t ' + str(self.__definition).replace('],', ']\n\t\t\t\t') + '\nPages:\t\t\t ' + str(self.__indices) + '\n'
        return '\nDefinitions:\t ' + str(self.__definition)[2:-2].replace('], [', ',\n\t\t\t\t ') + '\nPages:\t\t\t ' + str(self.__indices) + '\n'
        #return f'\nDefinition: {self.__definition} \nPages: {self.__indices}\n'
