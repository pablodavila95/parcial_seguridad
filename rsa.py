# Here we are going to convert the letters to numbers
import numpy as calculate


def alphabet():
    return {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u':30, 'v': 31, 'w': 32, 'x': 33, 'y':34, 'z': 35}


def convertToDecimal(plaintext):
    plaintext = plaintext.lower().strip()
    decimal = []
    for letter in plaintext:
        decimal.append(alphabet().get(letter))
    return ''.join(map(str, decimal))

print(convertToDecimal("ILLBEBACK"))

#C cipher, d private, n public
def decrypt(C):
    return calculate.mod(C^d, n)