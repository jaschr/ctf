#!/usr/bin/env

# Vigenere Cipher
# Enc: Ci = Ek(Mi) = (Mi + Ki) % 26
# Dec: Mi = Dk(Ci) = (Ci - Ki) % 26

initial_key = "CYLAB"

def generate_key(ciphertext, key):
    key = list(key)
    if len(ciphertext) == len(key):
        return(key)
    else:
        for i in range(len(ciphertext) - len(key)):
            key.append(key[i % len(key)])
        return "".join(key)

def decrypt(ciphertext, key):
    plaintext = []
    for i in range(len(ciphertext)):
        x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        plaintext.append(chr(x))
    return "".join(plaintext)

if __name__ == "__main__":
    with open("cipher.txt", 'r') as file:
        cipher = file.read()
    key = generate_key(cipher, initial_key)
    plaintext = decrypt(cipher, key)
    print(plaintext)
