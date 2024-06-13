def count_characters(word):
    result = {}
    for c in word:
        if c not in result:
            result[c] = 1
        else:
            result[c] = result[c] + 1

    return result

assert count_characters("Baby") == {'B': 1 , 'a': 1 , 'b': 1 , 'y': 1}
print(count_characters('smiles'))
