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
        self.__indices.add(indices)

    def __str__(self):
        return 'Definitions:\n' + str('\t\t\t\t\t' + self.__definition) + '\n\t\t\t\t\tPages:\n\t\t\t\t\t'\
            + (str(sorted(self.__indices))) + '\n\n'

