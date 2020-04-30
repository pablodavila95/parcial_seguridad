import random


def keygen(size):
    numbers = list(range(1, size + 1))
    random.shuffle(numbers)
    return numbers


def pretty_print(keygen):
    print(','.join(map(str, keygen)))


pretty_print(keygen(25))
