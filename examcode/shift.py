alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
sentence = list(input('Message:\n'))
ns = int(input('Key:\n'))
new_message = []

def shift(arr,letter, number):
    sn = (arr.index(letter) + number) % len(arr)
    return arr[sn]

def decrypt():
    invalphabet = alphabet
    invalphabet.reverse()
    for l in sentence:
        if l in invalphabet:
            new_message.append(shift(invalphabet,l, ns))
        else:
            new_message.append(l) 
    print(''.join(map(str, new_message)))

def encrypt():
    for l in sentence:
        if l in alphabet:
            new_message.append(shift(alphabet,l, ns))
        else:
            new_message.append(l) 
    print(''.join(map(str, new_message)))

def ask():
    i = input('Enter 1 to encrypt or 2 to decrypt the message\n')
    if i == "1":
        encrypt()
    elif i == "2":
        decrypt()
    else:
        ask()

ask()
