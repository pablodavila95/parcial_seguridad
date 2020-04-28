def decrypt(plaintext, key):
    plaintext = list(str(plaintext))
    key = list(str(key.strip()))
    ciphertext = []

    x = 0
    k = len(key)
    ntimes = int(len(plaintext)/k)
    for _ in range(0, ntimes):
        for i in range(0, k):
            lp = int(key[i]) + (k*x) - 1
            ciphertext.append(plaintext[lp])
        x += 1
    return(''.join(map(str, ciphertext)))


def encrypt(plaintext, key):
    plaintext = list(str(plaintext))
    key = list(str(key.strip()))
    ciphertext = []
    x = 0
    k = len(key)

    addL = True
    while addL:
        if len(plaintext) % k == 0:
            addL = False
        else:
            plaintext.append('-')

    ntimes = int(len(plaintext)/k)
    for _ in range(0, ntimes):
        for i in range(0, k):
            lp = int(key[i]) + (k*x) - 1
            ciphertext.append(plaintext[lp])
        x += 1
    return(''.join(map(str, ciphertext)))
