def sublist(char_list, chunk_size):
    return ([char_list[i * chunk_size:(i + 1) * chunk_size] for i in range((len(char_list) + chunk_size - 1) // chunk_size)])


def encrypt(plaintext, key):
    ciphertext = []
    if len(key) <= len(plaintext):
        plaintext = sublist(list(plaintext), len(key))
        i = 0
        for i in key:
            for row in plaintext:
                ciphertext.append(row[int(i)])

        return str(ciphertext)


print(encrypt(str(10100100), str(1234)))
