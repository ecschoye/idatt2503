import numpy as np

alphabet = "abcdefghijklmnopqrstuvwxyz"

K1 = "0123456789ABCDEF0123456789ABCDEF"
K2 = "1123456789ABCDEF0123456789ABCDEF"
x1 = "01000000000000000000000000000000"
x2 = "02000000000000000000000000000000"


def hex_to_bytes(hex):
    return bytes.fromhex(hex)

def hex_to_4x4matrix(hex_bytes):
    return np.array(list(hex_bytes)).reshape(4, 4).T

def bytes_to_matrix(byte_arr):
    return np.array(byte_arr, dtype=np.uint8).reshape(4, 4).T

def matrix_to_bytes(matrix):
    return matrix.T.reshape(16,).tobytes()

def matrix_to_hex(matrix):
    return matrix_to_bytes(matrix).hex()


K1 = hex_to_bytes(K1)
K2 = hex_to_bytes(K2)
x1 = hex_to_bytes(x1)
x2 = hex_to_bytes(x2)

def galois_multiplication(a, b):
    p = 0
    for counter in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x1b
        b >>= 1
    return p % 256


class AES:
    def __init__(self, key, state, n_rounds):
        self.key = np.array(key, dtype=np.uint8)
        self.state = np.array(state, dtype=np.uint8)
        self.rounds = n_rounds
        self.round_keys = self.key_expansion()

    s_box = (
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
        0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
        0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
        0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
        0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
        0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
        0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
    )

    rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]


    def add_round_key(self):
        self.state = self.state ^ self.key
        return self.state

    def sub_bytes(self):
        for i in range(4):
            for j in range(4):
                byte = self.state[i][j]
                high = (byte & 0xF0) >> 4
                low = byte & 0x0F
                self.state[i][j] = self.s_box[high * 16 + low]

        return self.state

    def shift_rows(self):
        for i in range(4):
            self.state[i] = np.roll(self.state[i], -i)

        return self.state

    def mix_columns(self):
        fixed_matrix = [
            [0x02, 0x03, 0x01, 0x01],
            [0x01, 0x02, 0x03, 0x01],
            [0x01, 0x01, 0x02, 0x03],
            [0x03, 0x01, 0x01, 0x02]
        ]
        result = np.zeros((4, 4), dtype=np.uint8)
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    result[i][j] ^= galois_multiplication(fixed_matrix[i][k], self.state[k][j])

        self.state = result

        return self.state

    def key_expansion(self):
        expanded_key = np.zeros((4, 4 * (self.rounds + 1)), dtype=np.uint8)
        expanded_key[:, :4] = self.key

        for i in range(4, 4 * (self.rounds + 1)):
            temp = expanded_key[:, i - 1].copy()

            if i % 4 == 0:
                temp = np.roll(temp, -1)

                for j in range(4):
                    high = (temp[j] & 0xF0) >> 4
                    low = temp[j] & 0x0F
                    temp[j] = AES.s_box[high * 16 + low]

                temp[0] ^= AES.rcon[i // 4 - 1]

            expanded_key[:, i] = expanded_key[:, i - 4] ^ temp

        return expanded_key

    def get_round_key(self, round):
        return self.round_keys[:, round * 4:(round + 1) * 4]

    def run(self):
        initial_round_key = self.get_round_key(0)
        for i in range(4):
            for j in range(4):
                self.state[i][j] ^= initial_round_key[i][j]

        for round_num in range(1, self.rounds + 1):
            self.sub_bytes()
            self.shift_rows()

            if round_num != self.rounds:
                self.mix_columns()

            round_key = self.get_round_key(round_num)
            for i in range(4):
                for j in range(4):
                    self.state[i][j] ^= round_key[i][j]

        return self.state


if __name__ == "__main__":
    initial_state = hex_to_4x4matrix(x1)
    initial_key = hex_to_4x4matrix(K1)

    # Displaying the initial key
    print("========= Initial Configuration =========")
    print(f"Initial key K1:")
    print(initial_key)
    print()

    # Displaying the initial state
    print(f"Initial state x1:")
    print(initial_state)
    print()

    print("========= One Round of AES Encryption =========")
    aes = AES(initial_key, initial_state, 1)
    final_state = aes.run()

    # Displaying the final state for one round of AES encryption
    final_state_hex = matrix_to_hex(final_state)
    print("Final state:")
    print(final_state)
    print()

    # Displaying the final state in hexadecimal format
    print(f"Final state in hex: {final_state_hex}")
    print()

    initial_state = hex_to_4x4matrix(x2)

    # Displaying the initial state
    print(f"Initial state x2:")
    print(initial_state)
    print()

    print("========= One Round of AES Encryption =========")
    aes = AES(initial_key, initial_state, 1)
    final_state = aes.run()
    print()

    # Displaying the final state for one round of AES encryption
    final_state_hex = matrix_to_hex(final_state)
    print("Final state:")
    print(final_state)
    print()

    # Displaying the final state in hexadecimal format
    print(f"Final state in hex: {final_state_hex}")
    print()




    print("========= Full AES Encryption =========")
    initial_key = hex_to_4x4matrix(K1)
    initial_state = hex_to_4x4matrix(x1)
    aes = AES(initial_key, initial_state, 10)
    final_state = aes.run()

    # Displaying the final state for full AES encryption
    print("Final state:")
    print(final_state)
    print()

    # Displaying the final state in hexadecimal format
    print(f"Final state in hex: {matrix_to_hex(final_state)}")

