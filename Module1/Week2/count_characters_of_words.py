def count_characters(word):
    result = {}
    for c in word:
        if c not in result:
            result[c] = 1
        else:
            result[c] = result[c] + 1

    return result

print(count_characters('smiles'))
