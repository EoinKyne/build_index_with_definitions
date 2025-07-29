import pytest
from build_index.build_index import Word


@pytest.fixture
def word_definition():
    d = "'Able a. To make able; to enable; to strengthen.'"
    return d


@pytest.fixture()
def word_index():
    index = 1
    return index


class TestWord:

    def test_set_definition(self, word_definition):
        word = Word("", set())
        word.set_definition(word_definition)
        assert word.get_definition() == "'Able a. To make able; to enable; to strengthen.'"

    def test_set_index(self, word_index):
        word = Word("", set())
        word.set_indices(word_index)
        assert word.get_indices() == {1}


