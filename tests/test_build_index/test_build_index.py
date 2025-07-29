import pytest
from pathlib import Path

from build_index.build_index import build_index

test_file = './tests/test_build_index_and_dictionary/test_book.txt'
skip_words = "The a is it for".lower()
dictionary = {'quick': "'Quick superl. Alive; living; animate; -- opposed to dead or   inanimate.\n\t\t\t\t\t', "
                       "'Quick superl. Characterized by life or liveliness; animated;   sprightly; agile; brisk; ready.\n\t\t\t\t\t', "
                       "'Quick superl. Speedy; hasty; swift; not slow; as, be quick.\n\t\t\t\t\t'",
              'moon': "'Moon n. The celestial orb which revolves round the earth; the   satellite of the earth; a secondary planet, whose light, borrowed from   the sun, is reflected to the earth, and serves to dispel the darkness   of night. The diameter of the moon is 2,160 miles, its mean distance   from the earth is 240,000 miles, and its mass is one eightieth that of   the earth. See Lunar month, under Month.\n\t\t\t\t\t', "
                      "'Moon n. A secondary planet, or satellite, revolving about any member   of the solar system; as, the moons of Jupiter or Saturn.\n\t\t\t\t\t', "
                      "'Moon n. The time occupied by the moon in making one revolution in her   orbit; a month.\n\t\t\t\t\t', "
                      "'Moon n. A crescentlike outwork. See Half-moon.\n\t\t\t\t\t'"}


def test_build_index():
    print(Path.cwd())
    index = build_index(test_file, dictionary, skip_words)

    assert 'quick' in index
    assert 'the' not in index
    assert "Characterized by life or liveliness" in index.get("quick").get_definition()
    assert index.get("quick").get_indices() == {1}
    assert "Undefined" in index.get("jumped").get_definition()
    assert index.get("jumped").get_indices() == {1}


def test_build_index_invalid_path():
    with pytest.raises(FileNotFoundError):
        file = "./invalid/path/book.txt"
        build_index(file, skip_words, dictionary)
