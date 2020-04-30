import csv
from permutation import encrypt

our_key = [12, 7, 16, 11, 23, 14, 10, 22, 13, 21, 19,
           1, 25, 5, 24, 15, 9, 20, 18, 3, 17, 6, 8, 4, 2]


def generate_ciphertexts(key, filename):
    ciphertexts = []
    with open('neuralnet/' + filename + '.csv', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            ciphertexts.append(
                encrypt(''.join(map(str, row)).replace(' ', ''), key))
    return ciphertexts


def write_csv(filename, key, source):
    with open('neuralnet/' + filename + '.csv', 'w') as result_file:
        wr = csv.writer(result_file, quoting=csv.QUOTE_NONE, escapechar=' ')
        for string in generate_ciphertexts(key, source):
            string = ','.join(map(str, string))
            wr.writerow([string])


#generate_ciphertexts(our_key, 'trainP')
write_csv('testC', our_key, 'testP')
