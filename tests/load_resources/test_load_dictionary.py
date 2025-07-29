import pytest

import load_resources.load_dictionary

csv_data = """word,wordtype,definition
Abandon,v. t.,To cast or drive out; to banish; to expel; to reject.
,v.,Abandonment; relinquishment.
Abate,v. t.,To beat down; to overthrow."""


def test_load_dictionary(mocker):
    mock_open = mocker.mock_open(read_data=csv_data)
    mocker.patch('builtins.open', mock_open)

    result = load_resources.load_dictionary.read_dictionary("./resources/dictionary/dictionary.csv")

    assert result == {'abandon': 'Abandon v. t. To cast or drive out; to banish; to expel; to reject.\n\t\t\t\t\t', '':
        'v. Abandonment; relinquishment.\n\t\t\t\t\t', 'abate': 'Abate v. t. To beat down; to overthrow.\n\t\t\t\t\t'}
    mock_open.assert_called_once_with("./resources/dictionary/dictionary.csv", "r")


def test_read_dictionary_invalid_path():
    with pytest.raises(FileNotFoundError):
        load_resources.load_dictionary.read_dictionary("./invalid/path/dictionary.csv")
