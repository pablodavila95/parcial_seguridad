alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = list(alphabet)
message = input('Message: \n')
message = message.replace(' ','')
message = list(message)
key = int(input('Key:\n'))
new_message = []

def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

def encrypt():
    for m in message:
        new_message.append(alphabet[(alphabet.index(m)*key)%26])
    print(''.join(map(str, new_message)))

def decrypt():
    nkey = modInverse(key,26)
    for m in message:
        new_message.append(alphabet[(alphabet.index(m)*nkey)%26])
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