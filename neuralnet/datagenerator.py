import csv
import random



def generate_data(filename, string_length, list_size):
    if string_length < 0 or list_size < 0:
        raise Exception("Values must be bigger than zero.")
    if not type(string_length) is int or not type(list_size) is int:
        raise TypeError("Only integers are allowed.")

    def write_csv(filename):
        with open('neuralnet/' + filename + '.csv', 'w') as result_file:
            wr = csv.writer(result_file, quoting=csv.QUOTE_NONE, escapechar=' ')
            for string in generate_binary_string_csv(string_length, list_size):
                wr.writerow([string])

    def generate_binary_string(length):
        generated_string = []
        for _ in range(length):
            generated_string.append(random.randint(0, 1))
        return ','.join(map(str, generated_string))

    def generate_binary_string_csv(string_length, list_size):
        strings_list = []
        for _ in range(list_size):
            strings_list.append(generate_binary_string(string_length))
        return strings_list

    filename = str(filename)

    write_csv(filename)


generate_data('testP', 25, 10000)
