from find_max_of_kernel import max_kernel
from count_characters_of_words import count_characters
from levenshtein_distance import levenshtein_distance

def test_max_kernel():
    num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
    k = 3
    expected_result = [5, 5, 5, 5, 10, 12, 33, 33]
    assert max_kernel(num_list, k) == expected_result

def test_count_characters_of_word():
    # Test case 1
    input_string = 'smiles'
    expected_result = {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
    assert count_characters(input_string) == expected_result

    # Test case 2
    input_string = 'Happiness'
    expected_result = {'H': 1 , 'a': 1 , 'e': 1 , 'i': 1 , 'n': 1 , 'p': 2 , 's': 2}
    assert count_characters(input_string) == expected_result

def test_levenshtein_distance():
    assert levenshtein_distance('hola', 'hello') == 3
