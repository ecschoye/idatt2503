def caesar_cipher(x):
    return (x + 3) % 32

def caesar_decipher(x):
    return (x - 3) % 32


def bit_xor(a, b):
    return a ^ b


alphabet = " abcdefghijklmnopqrstuvwxyzæøå,."

plaintext = "aaaaaa"
plaintext_2 = "dette er en test"
ciphertext = "qvxæyy hkgdgk,,oqhdnc"
block_size = 5
IV = 13


def encrypt(_plaintext):
    numbers = [alphabet.index(x) for x in _plaintext]

    encrypted_message = []
    previous_block = IV

    for i in range(0, len(numbers), block_size):
        # sublist containing numerical values for current block
        block = numbers[i:i + block_size]
        # xor with previous block
        xor_block = [bit_xor(x, previous_block) for x in block]
        # encrypted each element of xored block
        encrypted_block = [caesar_cipher(x) for x in xor_block]
        # update previous block to the last element of current encrypted block
        previous_block = encrypted_block[-1]
        # add encrypted block to encrypted message
        encrypted_message.extend(encrypted_block)

    encrypted_text = ''.join([alphabet[num] for num in encrypted_message])
    return encrypted_text

def decrypt(_ciphertext):
    numbers = [alphabet.index(x) for x in _ciphertext]

    decrypted_message = []
    previous_block = IV

    for i in range(0, len(numbers), block_size):
        block = numbers[i:i + block_size]
        decrypted_block = [caesar_decipher(x) for x in block]
        xor_block = [bit_xor(x, previous_block) for x in decrypted_block]
        previous_block = block[-1] if block else 0
        decrypted_message.extend(xor_block)

    decrypted_text = ''.join([alphabet[num] for num in decrypted_message])
    return decrypted_text


if __name__ == "__main__":
    print("=== Case 1: Encrypting 'aaaaaa' ===")
    print(f"Input Message: {plaintext}")
    encrypted_text = encrypt(plaintext)
    print(f"Encrypted Message: {encrypted_text}\n")

    print("Decrypting Back to Original Message")
    decrypted_text = decrypt(encrypted_text)
    print(f"Decrypted Message: {decrypted_text}\n")

    print("=== Case 2: Encrypting 'dette er en test' ===")
    print(f"Input Message: {plaintext_2}")
    encrypted_text = encrypt(plaintext_2)
    print(f"Encrypted Message: {encrypted_text}\n")

    print("Decrypting Back to Original Message")
    decrypted_text = decrypt(encrypted_text)
    print(f"Decrypted Message: {decrypted_text}\n")
    print()

    print("=== Case 3: Decrypting 'qvxæyy hkgdgk,,oqhdnc' ===")
    print(f"Input Cipher: {ciphertext}")
    decrypted_text = decrypt(ciphertext)
    print(f"Decrypted Message: {decrypted_text}\n")

    print("Encrypting Back to Original Cipher")
    encrypted_text = encrypt(decrypted_text)
    print(f"Encrypted Message: {encrypted_text}\n")
