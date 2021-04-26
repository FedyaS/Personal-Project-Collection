def combinations(alphabet, number_to_choose, prefix=[]):
    result = []
    new_alphabet = alphabet.copy()
    for i in range(0, len(alphabet)):
        prefix.append(alphabet[i])
        if number_to_choose == 1:
            result.append(prefix.copy())
        else:
            new_alphabet.pop(0)
            result.extend(combinations(new_alphabet, number_to_choose - 1, prefix))
        prefix.pop()
    return result


def permutations(alphabet, number_to_choose, prefix=[]):
    result = []
    for i in range(0, len(alphabet)):
        prefix.append(alphabet[i])
        if number_to_choose == 1:
            result.append(prefix.copy())
        else:
            new_alphabet = alphabet.copy()
            new_alphabet.pop(i)
            result.extend(permutations(new_alphabet, number_to_choose - 1, prefix))
        prefix.pop()
    return result


def factorial(number):
    if number > 1:
        return number*factorial(number-1)
    else:
        return 1


def number_of_permutations(n, r):
    """Returns # of permutations for nPr formula"""
    x = 1
    for number in range(n-r+1, n+1):
        x *= number
    return x


def number_of_combinations(n, r):
    """Returns # of combinations for nCr formula"""
    c = 1
    for number in range(n-r+1, n+1):
        c *= number
    z = factorial(r)
    a = c/z
    return a
