
def find_key(_p, _q, _e):
    phi = (_p - 1) * (_q - 1)

    for i in range(1, phi):
        if (i * _e) % phi == 1:
            return i


def check_if_signature_is_valid(_m, _s, _e, _n):
    return (_s ** _e) % _n == m

def encrypt(_m, _e, _n):
    return (_m ** _e) % _n

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
    print(f'is signature valid? {check_if_signature_is_valid(m, s, e, n)}')
    print()

    n_b = 3127
    e_b = 33
    # Steps to encrypt: message ** e_b % n_b
    print(f'encrypted message: {encrypt(m, e_b, n_b)}')
