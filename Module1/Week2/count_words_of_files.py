def count_words_from_file(file_path):
    result = {}
    with open(file_path, 'r') as file:
        for line in file:
            word_list = [word.lower() for word in line.split()]
            for word in word_list:
                if word in result:
                    result[word] = result[word] + 1
                else:
                    result[word] = 1

    return result

file_path = 'Module1/Week2/data.txt'
result = count_words_from_file(file_path)
print(result['man'])
