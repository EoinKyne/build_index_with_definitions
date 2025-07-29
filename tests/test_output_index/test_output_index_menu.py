import builtins
from pathlib import WindowsPath
from word import Word
import pytest
from output_index.output_index_and_dictionary import print_word_and_definition_to_console, write_index_to_text_file, print_index_to_console, get_titles


def test_print_word_and_definition_to_console(mocker):
    mocker.patch('builtins.input', return_value='Abode')
    mock_print = mocker.patch('builtins.print')
    w = Word("abode, ,pret. of abide.", set())
    dic = {"abode": w}

    print_word_and_definition_to_console(dic)
    mock_print.assert_has_calls([mocker.call('Word:\t\t\t\tDetails:\n')], [mocker.call('Abode\t\t\t\t Definitions:\n\t\t\t\t\tabode, ,pret. of abide.\n\t\t\t\t\tPages:\n\t\t\t\t\t[]\n')])


def test_write_to_file(mocker):
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    mocker.patch('builtins.input', return_value="filex")
    w = Word("abode, ,pret. of abide.", set())

    dic = {"Abode": w}
    write_index_to_text_file(dic)

    mock_open.assert_called_once_with(WindowsPath('D:/repositories/python/build_index_of_words_with_definitions/output/filex.txt'), 'w+')
    mock_open().write.assert_has_calls([mocker.call('Word:\t\t\t\tDetails:\n')], [
        mocker.call('Abode\t\t\t\t Definitions:\n\t\t\t\t\tabode, ,pret. of abide.\n\t\t\t\t\tPages:\n\t\t\t\t\t[]\n')])


def test_print_index_to_console(mocker):
    mock_print = mocker.patch('builtins.print')

    w = Word("abode, ,pret. of abide.", set())
    dic = {"Abode": w}

    print_index_to_console(dic)
    mock_print.assert_has_calls([mocker.call('Word:\t\t\t\tDetails:\n')], [
        mocker.call('Abode\t\t\t\t Definitions:\n\t\t\t\t\tabode, ,pret. of abide.\n\t\t\t\t\tPages:\n\t\t\t\t\t[]\n')])


def test_get_titles():
    assert get_titles() == f'Word:\t\t\t\tDetails:\n'
