def caesar_cipher(x):
    return (x + 3) % 32

def caesar_decipher(x):
    return (x + 32 - 3) % 32


def bit_xor(a, b):
    return a ^ b


alphabet = " abcdefghijklmnopqrstuvwxyzæøå,."

plaintext = "aaaaaa"
plaintext_2 = "dette er en test"
ciphertext = "qvxæyy hkgdgk,,oqhdnc"
block_size = 5
IV = 13


def encrypt(_plaintext):
    encrypted_message = []
    previous_block = IV

    for i in range(len(_plaintext)):
        block = alphabet.index(_plaintext[i])
        char = alphabet[caesar_cipher(bit_xor(block, previous_block))]
        previous_block = alphabet.index(char)
        encrypted_message.append(char)

    encrypted_text = ''.join(encrypted_message)
    return encrypted_text

def decrypt(_ciphertext):
    decrypted_message = []
    previous_block = IV

    for i in range(len(_ciphertext)):
        block = alphabet.index(_ciphertext[i])
        char = alphabet[bit_xor(caesar_decipher(block), previous_block)]
        previous_block = alphabet.index(_ciphertext[i])
        decrypted_message.append(char)
    
    decrypted_text = ''.join(decrypted_message)
    return decrypted_text


if __name__ == "__main__":
    print("=== Case 1: Encrypting 'aaaaaa' ===")
    print(f"Input Message: {plaintext}")
    encrypted_text = encrypt(plaintext)
    print(f"Encrypted Message: {encrypted_text}\n")

    print("=== Case 2: Encrypting 'dette er en test' ===")
    print(f"Input Message: {plaintext_2}")
    encrypted_text = encrypt(plaintext_2)
    print(f"Encrypted Message: {encrypted_text}\n")

    print("=== Case 3: Decrypting 'qvxæyy hkgdgk,,oqhdnc' ===")
    print(f"Input Cipher: {ciphertext}")
    decrypted_text = decrypt(ciphertext)
    print(f"Decrypted Message: {decrypted_text}\n")
