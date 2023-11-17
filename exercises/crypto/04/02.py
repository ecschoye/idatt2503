import numpy as np


def fermat_factorization(_n):
    _a = np.ceil(np.sqrt(_n))
    _b = np.sqrt(_a ** 2 - _n)
    _count = 0
    while not _b.is_integer():
        _count += 1
        if _a > _b:
            _a += 1
            _b = np.sqrt(_a ** 2 - _n)
            continue
        else:
            return None, None, _count

    return int(_a - _b), int(_a + _b), _count


def extended_euclidean_algorithm(_a, _b):
    r = [_a, _b]
    _s = [1, 0]
    _t = [0, 1]
    i = 2
    q = [0, 0]
    while r[i - 1] != 0:
        q.append(r[i - 2] // r[i - 1])
        r.append(r[i - 2] % r[i - 1])
        _s.append(_s[i - 2] - q[i] * _s[i - 1])
        _t.append(_t[i - 2] - q[i] * _t[i - 1])
        i += 1

    return r[i - 2], _s[i - 2], _t[i - 2]


def repeated_squaring(_b, _e, _n):
    if _e == 0:
        return 1
    if _e == 1:
        return _b % _n

    t = repeated_squaring(_b, _e // 2, _n)
    t = (t * t) % _n

    if _e % 2 == 0:
        return t
    else:
        return ((_b % _n) * t) % _n


if __name__ == "__main__":
    prime_factor_p = 1283
    divisors = [1307, 1879, 2003, 2027]
    highest_iteration_count = 0
    x = None
    y = None
    for idx, divisor in enumerate(divisors, start=1):
        n = prime_factor_p * divisor
        print(f"\nn_{idx} = ", n)
        factor_a, factor_b, iterations = fermat_factorization(n)

        if factor_a and factor_b:
            print(f"n_{idx} factorized: {factor_a} * {factor_b} = {n}")
            phi_n = -((factor_a - 1) * (factor_b - 1))
            print(f"φ(n_{idx}) = {phi_n}")
            gcd, e, _ = extended_euclidean_algorithm(3, phi_n)
            print(f"e_{idx} = {e}")
        else:
            print(f"n_{idx} could not be factorized using Fermat's method.")

        print(f"Number of iterations: {iterations}")

        if iterations > highest_iteration_count:
            x = factor_a
            y = factor_b
            highest_iteration_count = iterations
    # gcd, e, _ = extended_euclidean_algorithm(3, -2597332)

    # Find the corresponding public key e using the extended Euclidean algorithm. Write a program to do the calculation.
    print("\nTask B")
    a = 111
    e = 865777
    mod = x * y
    print(f"message encrypted with repeated squaring:", repeated_squaring(a, e, mod))
