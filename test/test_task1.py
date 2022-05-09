from task1 import length_longest_substring
import pytest


def test_examples():
    # this data set tests cases of examples given in task
    assert length_longest_substring("abcabcbb") == 3
    assert length_longest_substring("bbbbb") == 1


def test_one_letter_string():
    # this data set tests cases of one letter strings input
    assert length_longest_substring("a") == 1
    assert length_longest_substring("z") == 1
    assert length_longest_substring("$") == 1


def test_string_including_numbers():
    # this data set tests cases of strings which include numbers in input
    assert length_longest_substring("1234aaaaa") == 5
    assert length_longest_substring("12aaaaa") == 3
    assert length_longest_substring("11a") == 2


def test_wrong_input():
    #  this data set tests bad input cases
    with pytest.raises(TypeError):
        length_longest_substring(123)
    with pytest.raises(TypeError):
        length_longest_substring(['avd2'])
    with pytest.raises(TypeError):
        length_longest_substring((1, "abc"))
    with pytest.raises(TypeError):
        length_longest_substring(10.0)
