import numpy as calculate
import math



def alt_find_secret_key_with_A_g_p(b):
    A = 573450335
    g = 642281
    p = 682950071

    B = calculate.mod(pow(g, b), p)
    return calculate.mod(pow(A, b), p)

def find_secret_key(p, g):
    a = int(input("Enter alice's secret number"))
    A = calculate.mod(p, pow(g, a))
    print("Alice sends Bob A = " + str(A))

    b = int(input("Enter bob's secret number'"))
    B = calculate.mod(p, pow(b, a))
    print("Bob sends Alice B = " + str(B))

    s_alice = calculate.mod(p, pow(B, a))
    s_bob = calculate.mod(p, pow(A, b))

    if s_alice == s_bob:
        s = s_alice
        return s
    else:
        return print("Something went wrong when calculating secret key")