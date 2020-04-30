from csv import reader, writer
from permutation import encrypt

our_key = [12, 7, 16, 11, 23, 14, 10, 22, 13, 21, 19,
           1, 25, 5, 24, 15, 9, 20, 18, 3, 17, 6, 8, 4, 2]


def generate_ciphertexts(key):
    ciphertexts = []
    with open('neuralnet/trainP.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            ciphertexts.append(encrypt(''.join(map(str, row)), key))
    return ciphertexts


def write_csv(filename, key):
    with open('neuralnet/' + filename + '.csv', 'w') as result_file:
        wr = writer(result_file)
        for string in generate_ciphertexts(key):
            wr.writerow([string, ])


write_csv('trainC', our_key)
