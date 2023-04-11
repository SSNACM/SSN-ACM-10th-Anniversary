import ecdsa as e
import ecdsa.util as eu
import secrets
import timeit

def generate_key(length):
    return secrets.randbelow(length)

def encryption(message):
    global k
    curve = e.curves.SECP256k1
    g = curve.generator
    order_of_curve = curve.order
    k = secrets.randbelow(order_of_curve-1) + 1
    public_key = g.x() * k
    secret_key = k * public_key

    otp = [secrets.randbelow(len(message)) for _ in range(len(message))] # generate one-time pad
    keys = [generate_key(len(message)) for _ in range(len(message))] # generate random keys

    encrypt_msg = ""
    for i, char in enumerate(message):
        shift = (keys[i % len(keys)] + otp[i]) % 26 # add one-time pad to shift
        encrypt_msg += caesar_cipher(char, shift)

    print("Encrypted message using rotating shift keying caesar cipher and one time pad, before converting it to point :", encrypt_msg)

    point = 0
    for char in encrypt_msg:
        point = point * 1000 + ord(char)

    sp = public_key*secret_key
    sg = secret_key*g.x()
    encrypted_point = point + sp

    return (sg,encrypted_point, otp, keys) # return one-time pad and keys with encrypted message

def decryption(encrypted_msg, otp, keys):
    sg = encrypted_msg[0]
    encrypted_point = encrypted_msg[1]

    encrypted_point = encrypted_point - (sg * k)
    real_msg = ""
    while encrypted_point > 0:
        real_msg = chr(encrypted_point % 1000) + real_msg  
        encrypted_point = encrypted_point // 1000  

    decrypt_msg = ""
    for i, char in enumerate(real_msg):
        shift = (keys[i % len(keys)] + otp[i]) % 26 # add one-time pad to shift
        decrypt_msg += caesar_cipher(char, -shift) # use negative shift to decrypt

    return decrypt_msg

def caesar_cipher(char, key):
    if 32 <= ord(char) <= 126:  
        shift = key % 95  
        char_num = ord(char) - 32  
        shifted_num = (char_num + shift) % 95
        shifted_char = chr(shifted_num + 32)  
        return shifted_char
    else:
        return char


if __name__ == "__main__":
    message = "!-- $ Hello 1234 -- !#" 
    ency = encryption(message)
    time_taken = timeit.timeit(lambda: encryption(message), number=100)
    print(time_taken)
    print("Encrypted message:", ency[1])
    print("One-time pad:", ency[2])
    print("Keys:", ency[3])

    decy = decryption(ency, ency[2], ency[3])
    print("Decrypted message:", decy)
