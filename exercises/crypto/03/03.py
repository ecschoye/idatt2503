def e_3(_x):
    return (_x + 3) % 2 ** 8

def e_3_inv(_x):
    return (_x + 256 - 3) % 2 ** 8


def xor(a, b):
    return a ^ b


def cbc_mac(_x, block_size=4):
    IV = 0
    y = IV

    length = len(format(_x, '016b'))

    for i in range(0, length, block_size):
        x_block = (_x >> 16 - block_size - i) & 0b1111
        print(f"Block: {format(x_block, '04b')}")
        y = e_3(xor(x_block, y))

    return y


def cbc_mac_inv(_x, block_size=4):
    IV = 0
    y = IV

    length = len(format(_x, '016b'))

    for i in range(0, length, block_size):
        x_block = (_x >> 16 - block_size - i) & 0b1111
        print(f"Block: {format(x_block, '04b')}")
        y = e_3_inv(xor(x_block, y))

    return y


if __name__ == '__main__':
    """
    Use the Caesar cipher, with encryption e3(x) = x + 3 (mod 28) and find the CBC-MAC to the following two messages:
    """
    x = 0b1101111110100001
    x_prime = 0b0010110000011111

    print(f"Message x: {format(x, '016b')}")
    print(f"CBC-MAC x: {format(cbc_mac(x), '08b')}")
    print()

    # Not sure if it meant to be CBC-MAC of x prime with e_3 or e_3_inv
    print(f"Message x': {format(x_prime, '016b')}")
    print(f"CBC-MAC x': {format(cbc_mac(x_prime), '08b')}")
    print()
    print(f"Message x': {format(x_prime, '016b')}")
    print(f"CBC-MAC inv x': {format(cbc_mac_inv(x_prime), '08b')}")
