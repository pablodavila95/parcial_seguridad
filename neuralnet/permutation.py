def decrypt(plaintext, key):
    plaintext = list(plaintext)
    key = list(key.strip())
    ciphertext = []

    x = 0
    k = len(key)
    ntimes = int(len(plaintext)/k)
    for w in range(0, ntimes):
        for i in range(0, k):
            lp = int(key[i]) + (k*x) - 1
            ciphertext.append(plaintext[lp])
        x += 1
    return(''.join(map(str, ciphertext)))


def encrypt(plaintext, key):
    plaintext = list(plaintext)
    key = list(key.strip())
    ciphertext = []

    addL = True
    while addL:
        if len(plaintext) % len(key) == 0:
            addL = False
        else:
            plaintext.append('-')
    x = 0
    k = len(key)
    ntimes = int(len(plaintext)/k)
    for w in range(0, ntimes):
        for i in range(0, k):
            lp = int(key[i]) + (k*x) - 1
            ciphertext.append(plaintext[lp])
        x += 1
    return(''.join(map(str, ciphertext)))
