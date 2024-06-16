from find_max_of_kernel import max_kernel
from count_characters_of_words import count_characters
from count_words_of_files import count_words_from_file
from levenshtein_distance import levenshtein_distance
from multiple_choices_questions import (
    check_the_number,
    append_min_max,
    extend_list,
    find_min_in_list,
    find_max_in_list,
    check_equal_num,
    find_mean,
    check_if_divisible_by_three,
    factorial,
    reverse_string,
    my_function,
    find_unique_num,
)

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

def test_count_words_of_file():
    file_path = 'Module1/Week2/data.txt'
    result = count_words_from_file(file_path)
    assert result['man'] == 6

def test_levenshtein_distance():
    assert levenshtein_distance('hola', 'hello') == 3

def test_check_the_number():
    assert check_the_number(2) == "True"
    assert check_the_number(6) == "False"

def test_append_min_max():
    data = [10, 2, 5, 0, 1]
    max_val = 2
    min_val = 1
    expected_result = [2, 2, 2, 1, 1]
    assert append_min_max(data, max_val, min_val) == expected_result

def test_extend_list():
    list_num1 = [1, 2]
    list_num2 = [3, 4]
    expected_result = [1, 2, 3, 4]
    assert extend_list(list_num1, list_num2) == expected_result

def test_find_min_in_list():
    my_list = [1, 2, 3, -1]
    assert find_min_in_list(my_list) == -1

def test_find_max_in_list():
    my_list = [1, 9, 9, 0]
    assert find_max_in_list(my_list) == 9

def test_check_equal_num():
    my_list = [1, 2, 3, 4]
    assert check_equal_num(my_list, 2) == True
    assert check_equal_num(my_list, 5) == False

def test_find_mean():
    my_list = [0, 1, 2]
    assert find_mean(my_list) == 1

def test_check_if_divisible_by_three():
    data = [1, 2, 3, 5, 6]
    expected_result = [3, 6]
    assert check_if_divisible_by_three(data) == expected_result

def test_factorial():
    assert factorial(4) == 24

def test_reverse_string():
    x = 'apricot'
    assert reverse_string(x) == 'tocirpa'

def test_my_function():
    data = [2, 3, 5, -1]
    expected_result = ['T', 'T', 'T', 'N']
    assert my_function(data) == expected_result

def test_find_unique_num():
    lst = [9, 9, 8, 1, 1]
    expected_result = [9, 8, 1]
    assert find_unique_num(lst) == expected_result