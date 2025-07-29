import pytest
import load_resources.load_skip_words


def test_load_skip_words(mocker):
    mock_open = mocker.mock_open(read_data='any, anything, else')
    mocker.patch('builtins.open', mock_open)

    result = load_resources.load_skip_words.load_skip_words("./resources/ignore_words/IgnoreWords.txt")

    assert result == 'any, anything, else'
    mock_open.assert_called_once_with("./resources/ignore_words/IgnoreWords.txt", "r")


def test_load_skip_words_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_resources.load_skip_words.load_skip_words("./invalid/path/IgnoreWords.txt")