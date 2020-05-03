# Respuestas a examen parcial
*Equipo: Eduardo Giadáns Zárate - A01411416
         Pablo Emilio Dávila Rodríguez - A00513157
         Rodrigo Rivera Guevara - A07025360*

1.
    - A.  
        
        Alice sends Bob A = 573450335,
        Bob's secret number = 544097,
        Bob sends Alice B = 337242414,
        The private key is : 
        661737200

    - B.  033040811485173401

2.  
    - A.  
        - 1. Ciphertext: GAMDXCJUPOCHCYEDXMUK Key = 7 Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
            len(Alphabet) = 26

        - 2. Get inv modulo of the key and alphabet length:
             inverse of (a)mod(c) is the value b that makes (a * b) % c == 1
             going trough values 0 to C-1 we find that the b that makes ((a * b) % c == 1) is 15
        - 3. We use 15 as our new key
        - 4. For every letter -> new letter is alphabet.index(letter in message)*nkey)%a.len:
        
                                     Cipher: G A M  D X  C J U  P  O  C H C Y  E D X  M  U  K indexes of letters in Cipher: 6,0,12,3,23,2,9,20,15,14,2,7,2,24,4,3,23,12,20,10
                   indexes after conversion: 12,0,24,19,7,4,5,14,17,2,4,1,4,22,8,19,7,24,14,20
                     indexes to new letters: M  A Y  T  H E F O  R  C E B E W  I T  H Y  O  U
                    
        - 5. plaintext -> MAYTHEFORCEBEWITHYOU

    
    - B.  
          IDONTKNOWRICKITLOOKSFAKE -> QGCAMUACSIQEUQMWCCUKKAUI
          QGCAMUACSIQEUQMWCCUKKAUI -> QGCAMUACSIQEUQMWCCUKKAUI

          The multiplicative inverse of “a modulo m” exists only if a and m are relatively prime,
          that means that the gcd of "a" and "b" must be 1. In this case, 2 and 26 have a gcd of 2
          so the inverse doesn't exist and the text can't be decrypted

3.  
    - A.  
        IVXRVVWSKX Key: 5 -> NACWAABXPC != CPXBAAWCAN 
        VSMRSLGGMBRBXBZIENHCYY Key: 5 -> AXRWXQLLRGWGCGENJSMHDD != AXRWQXLLRGXGCGENJSMHDP

    - B.  YOUCOMPLETEME
          MAXIMUSDECIMUSMERIDIUS

4.
    - A.  Hexadecimal alphabet = {'0123456789ABCDEF'} len(Alphabet) = 16 len(Ciphertext) = 20
          Worst-case scenario takes place when the length of the key equals the length of the plaintext
          so len(key) = len(Ciphertext)
          
          keys = number of choices in alphabet ^  number of choices in key which is len(key)
          keys = 16^20 = 1.208925819614629174706176 × 10^24 keys

    - B.  Worst-case scenario, the last key analyzed is the correct key
          so Time = (1.208925819614629174706176 × 10^24) * 0.15ms

          Time = 1.813×10^23 ms
          according to wolfram, that's about 5.746×10^12 average Gregorian years

    - C.  If you convert Hexadecimal to binary, for every letter you will have 4 binary digits
          meaning the key length changes to 20 letters * 4 digits = 80 digits.
          However, 80 digits with 2 choices {0,1} are 2^80 = 1.208925819614629174706176 × 10^24 keys
          which is the same as keeping it in hexadecimal


5.  
    - A.  On systems with limited capabilities to execute logic or bitwise operations. Also AND is       potentially and irreversible operation and might not be appropriate for encryption.


    - B.  It has worse security than the XOR version since it is more likely to have unflipped bits and could potentially show the information partially, which may make it easier to interpet. Will not actually work correctly with AND operator.

    - C.  It is not a safer option.

6.  
    - A.  If key size is k, there can be 2^k.

    - B.  If the key length is 10, the number of combinations is 2^10.

    - C.  It is the same as in the one-time pad cipher, 2^10. Based on the formula defined in A.

    >> Incorrecto. El problema es que muchas de las llaves darán como resultado repeticiones en el texto cifrado, lo que reduce significativamente el número de textos cifrados únicos que pueden producirse al usar el encriptador de permutataciones.

    - D.  Because we are using binary, it produces the same degree of security as the one-time pad cipher (the safest encryption) so we can argue that permutation cipher is safe in this case.

    >> Incorrecto. Al corregir la pregunta 6C verán las razones.

7.  
    - A.  We can decipher the key bits with the exposed plaintext using XOR to reverse the operation bit by bit. Using this we know so far that the key is 
        1-01. To obtain the second bit in the key, we would need to reverse the operation with XOR using another plaintext but we don't have it. If we had a
        complete english alphabet, we could maybe interpret the word using the human understanding of language. Since we are talking about bits, we cannot guess
        what the answer is. 

8.  
    - A.  The encrypted message for Alice is: 343231970106150475720500

    - B.  
        
        p = 805853
        q = 1012093
        n = 815598180329
        phi = 815596362384
        e = 65537
        d = 207791208977
        Bob's public key = (815598180329, 65537)
        Bob's private key = (815598180329, 207791208977)
        

    - C.  The string to send is 182121111 411101220. To encrypt, Alice would take the public key from Bob and use it to encrypt the message with the caveat that the message will
        be split in 2 to fit inside the RSA key length (Bob's key is quite short).
        This will result in the following string: 512390927633 249267066817. To decrypt, Bob would use his private key and his public key combined to get the original message.
        (after changing the numbers to letters back again, one string at a time with the same parameters).