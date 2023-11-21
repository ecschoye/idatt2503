"""
Alice uses p=47, q=83, e=3 as the public key for her RSA-based signature.

1. What is Alice's private key?
2. Verify if 964 is a valid signature for the message m=100.
3. Alice wants to encrypt and sign the message 100 to Bob. What are the exact steps?
   Assume Bob has the RSA with public key (n_b, e_b) = (3127, 33).
"""

def find_key(_p, _q, _e):
    phi = (_p - 1) * (_q - 1)

    for i in range(1, phi):
        if (i * _e) % phi == 1:
            return i


def check_if_signature_is_valid(_m, _s, _e, _n):
    return pow(_s, _e, _n) == _m


def sign_message(_m, _d, _n):
    return pow(_m, _d, _n)


def encrypt_message(_m, _e, _n):
    return pow(_m, _e, _n)


if __name__ == '__main__':
    p = 47
    q = 83
    n = p * q
    e = 3
    d = find_key(p, q, e)
    print(f'p = {p}, q = {q}, e = {e}, d = {d}')
    print()

    m = 100
    s = 964
    valid_signature = check_if_signature_is_valid(m, s, e, n)
    print(f'is signature valid? {valid_signature}')
    print()

    n_b = 3127
    e_b = 33
    # Steps to sign: message ** d % n
    signed_message = sign_message(m, d, n)
    print(f'signed message: {signed_message}')

    # Steps to encrypt: encrypted_message ** e_b % n_b
    encrypted_message = encrypt_message(signed_message, e_b, n_b)
    print(f'decrypted message: {encrypted_message}')
