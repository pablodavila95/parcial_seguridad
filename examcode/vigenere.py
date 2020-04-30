alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
key = list(input('Key:\n'))
message = list(input('Message:\n'))
skey = []
new_message = []

for w in key:
    skey.append(alphabet.index(w))

def shift(arr,letter,x):
    sn = (arr.index(letter) + skey[(x % len(skey))]) % len(arr)
    return arr[sn]

def encrypt():
    x = 0
    for w in message:
        if w in alphabet:
            new_message.append(shift(alphabet,w,x))
        else:
            new_message.append(w)
        x += 1
    print(''.join(map(str, new_message)))

def decrypt():
    invalphabet = alphabet
    invalphabet.reverse()
    x = 0
    for w in message:
        if w in invalphabet:
            new_message.append(shift(invalphabet,w,x))
        else:
            new_message.append(w)
        x += 1
    print(''.join(map(str, new_message)))

def ask():
    i = input('Enter 1 to encrypt or 2 to decrypt the message\n')
    if i == '1':
        encrypt()
    elif i == '2':
        decrypt()
    else:
        ask()
ask()