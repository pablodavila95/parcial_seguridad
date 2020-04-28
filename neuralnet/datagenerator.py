import csv
import random
import os


def generate_binary_string(length):
    if length < 0:
        raise Exception("Values must be bigger than zero.")
    if not type(length) is int:
        raise TypeError("Only integers are allowed.")

    generated_string = []
    for _ in range(length):
        generated_string.append(random.randint(0, 1))
    return ''.join(map(str, generated_string))


def generate_binary_string_csv(string_length, list_size):
    if string_length < 0 or list_size < 0:
        raise Exception("Values must be bigger than zero.")
    if not type(string_length) is int or not type(list_size) is int:
        raise TypeError("Only integers are allowed.")

    strings_list = []
    for _ in range(list_size):
        strings_list.append(generate_binary_string(string_length))
    return strings_list


def generate_data(filename, string_length, list_size):
    if string_length < 0 or list_size < 0:
        raise Exception("Values must be bigger than zero.")
    if not type(string_length) is int or not type(list_size) is int:
        raise TypeError("Only integers are allowed.")

    filename = str(filename)

    with open('neuralnet/' + filename + '.csv', 'w') as result_file:
        wr = csv.writer(result_file)
        for string in generate_binary_string_csv(string_length, list_size):
            wr.writerow([string,])

generate_data('test', 25, 10000)