from AES import AES
import numpy as np

alphabet = "abcdefghijklmnopqrstuvwxyz"

K1 = "0123456789ABCDEF0123456789ABCDEF"
K2 = "1123456789ABCDEF0123456789ABCDEF"
x1 = "01000000000000000000000000000000"
x2 = "02000000000000000000000000000000"


def hex_to_4x4matrix(hex_bytes):
    return np.array(list(hex_bytes)).reshape(4, 4).T


def matrix_to_bytes(matrix):
    return matrix.T.reshape(16, ).tobytes()


def matrix_to_hex(matrix):
    return matrix_to_bytes(matrix).hex()


def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)


K1 = hex_to_bytes(K1)
K2 = hex_to_bytes(K2)
x1 = hex_to_bytes(x1)
x2 = hex_to_bytes(x2)


def bytes_to_hex(bytes_value):
    return bytes_value.hex()


def is_coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1


def compare_bits(hex1, hex2):
    bits1 = bin(int(hex1, 16))[2:].zfill(128)
    bits2 = bin(int(hex2, 16))[2:].zfill(128)

    count = 0
    for i in range(len(bits1)):
        if bits1[i] != bits2[i]:
            count += 1

    return count


def xor_operation(message, key):
    encrypted_message = []
    for i in range(len(message)):
        message_byte = message[i]
        key_byte = key[i]
        encrypted_byte = message_byte ^ key_byte
        encrypted_message.append(encrypted_byte)

    return bytes(encrypted_message)


def affine_cipher(message, key):
    a = key[0]
    b = key[1]

    if not is_coprime(a, 256):
        raise ValueError("The value of 'a' must be coprime with 256.")

    encrypted_message = []
    for byte in message:
        transformed_byte = (a * byte + b) % 256
        encrypted_message.append(transformed_byte)

    return bytes(encrypted_message)


def encrypt_and_compare_a(message1, message2, key, cipher_func, cipher_name):
    encrypted1 = cipher_func(message1, key)
    encrypted2 = cipher_func(message2, key)

    hex1 = bytes_to_hex(encrypted1)
    hex2 = bytes_to_hex(encrypted2)

    print(f"Encrypted {cipher_name} x1 with k1: {hex1}")
    print(f"Encrypted {cipher_name} x2 with k1: {hex2}")
    print(f"Number of different bits: {compare_bits(hex1, hex2)}")
    print(f"Diffusion: {assess_diffusion(compare_bits(hex1, hex2), 128)}\n")


def encrypt_and_compare_b(message, key1, key2, cipher_func, cipher_name):
    encrypted1 = cipher_func(message, key1)
    encrypted2 = cipher_func(message, key2)

    hex1 = bytes_to_hex(encrypted1)
    hex2 = bytes_to_hex(encrypted2)

    print(f"Encrypted {cipher_name} x1 with k1: {hex1}")
    print(f"Encrypted {cipher_name} x1 with k2: {hex2}")
    print(f"Number of different bits: {compare_bits(hex1, hex2)}")
    print(f"Diffusion: {assess_key_sensitivity(compare_bits(hex1, hex2), 128)}\n")


def assess_diffusion(diff_bits, total_bits):
    percent_diff = (diff_bits / total_bits) * 100

    if percent_diff > 50:
        return "Excellent diffusion"
    elif percent_diff > 30:
        return "Good diffusion"
    elif percent_diff > 10:
        return "Moderate diffusion"
    elif percent_diff > 0:
        return "Poor diffusion"
    else:
        return "No diffusion"


def assess_key_sensitivity(diff_bits, total_bits):
    percent_diff = (diff_bits / total_bits) * 100

    if percent_diff > 50:
        return "Excellent key sensitivity"
    elif percent_diff > 30:
        return "Good key sensitivity"
    elif percent_diff > 10:
        return "Moderate key sensitivity"
    elif percent_diff > 0:
        return "Poor key sensitivity"
    else:
        return "No key sensitivity"


def xor_encryption(task):
    if task == 'a':
        encrypt_and_compare_a(x1, x2, K1, xor_operation, "xor")
    elif task == 'b':
        encrypt_and_compare_b(x1, K1, K2, xor_operation, "xor")


def affine_encryption(task,):
    if task == 'a':
        encrypt_and_compare_a(x1, x2, K1, affine_cipher, "affine")
    elif task == 'b':
        encrypt_and_compare_b(x1, K1, K2, affine_cipher, "affine")


def one_round_aes_encryption(task):
    if task == 'a':
        print("One Round of AES on x1 using K1")
        initial_state = hex_to_4x4matrix(x1)
        initial_key = hex_to_4x4matrix(K1)
        aes = AES(initial_key, initial_state, 1)
        final_state = aes.run()
        print(f"Final state in hex: {matrix_to_hex(final_state)}")
        print()

        print("One Round of AES on x2 using K1")
        initial_state = hex_to_4x4matrix(x2)
        aes = AES(initial_key, initial_state, 1)
        final_state2 = aes.run()
        print(f"Final state in hex: {matrix_to_hex(final_state2)}")
        diffusion = compare_bits(matrix_to_hex(final_state), matrix_to_hex(final_state2))
        print(f"Number of different bits: {diffusion}")
        print(f"Diffusion: {assess_diffusion(diffusion, 128)}")
        print()
    elif task == 'b':
        print("One Round of AES on x1 using K1")
        initial_state = hex_to_4x4matrix(x1)
        initial_key = hex_to_4x4matrix(K1)
        aes = AES(initial_key, initial_state, 1)
        final_state = aes.run()
        print(f"Final state in hex: {matrix_to_hex(final_state)}")
        print()

        print("One Round of AES on x1 using K2")
        initial_key = hex_to_4x4matrix(K2)
        aes = AES(initial_key, initial_state, 1)
        final_state2 = aes.run()
        print(f"Final state in hex: {matrix_to_hex(final_state2)}")
        diffusion = compare_bits(matrix_to_hex(final_state), matrix_to_hex(final_state2))
        print(f"Number of different bits: {diffusion}\n")
        print(f"Diffusion: {assess_key_sensitivity(diffusion, 128)}")
        print()


def full_aes_encryption(task):
    if task == 'a':
        print("Full AES on x1 using K1")
        initial_state = hex_to_4x4matrix(x1)
        initial_key = hex_to_4x4matrix(K1)
        aes = AES(initial_key, initial_state, 10)
        final_state = aes.run()
        print(f"Final state in hex: {matrix_to_hex(final_state)}")
        print()

        print("Full AES on x2 using K1")
        initial_state = hex_to_4x4matrix(x2)
        aes = AES(initial_key, initial_state, 10)
        final_state2 = aes.run()
        print(f"Final state in hex: {matrix_to_hex(final_state2)}")
        diffusion = compare_bits(matrix_to_hex(final_state), matrix_to_hex(final_state2))
        print(f"Number of different bits: {diffusion}")
        print(f"Diffusion: {assess_diffusion(diffusion, 128)}")
        print()
    elif task == 'b':
        print("Full AES on x1 using K1")
        initial_state = hex_to_4x4matrix(x1)
        initial_key = hex_to_4x4matrix(K1)

        aes = AES(initial_key, initial_state, 10)
        final_state = aes.run()
        print(f"Final state in hex: {matrix_to_hex(final_state)}")
        print()

        print("Full AES on x1 using K2")
        initial_key = hex_to_4x4matrix(K2)
        aes = AES(initial_key, initial_state, 10)
        final_state2 = aes.run()
        print(f"Final state in hex: {matrix_to_hex(final_state2)}")
        diffusion = compare_bits(matrix_to_hex(final_state), matrix_to_hex(final_state2))
        print(f"Number of different bits: {diffusion}")
        print(f"Diffusion: {assess_key_sensitivity(diffusion, 128)}")


if __name__ == '__main__':
    # Task 2a
    print(
        "a) For each cipher above, encrypt both x1 and x2, using the key K1 and compare the results, with regards to diffusion.\n")
    xor_encryption('a')
    affine_encryption('a')
    one_round_aes_encryption('a')
    full_aes_encryption('a')

    # Task 2b
    print("b) For each cipher, encrypt x1 using K1 and K2, and compare the results. How many bits change?\n")
    xor_encryption('b')
    affine_encryption('b')
    one_round_aes_encryption('b')
    full_aes_encryption('b')
