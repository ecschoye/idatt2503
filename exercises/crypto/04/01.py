"""
Task 1
Factorize n = 275621053.
You can assume that n = pq, where p−q is relatively small.
Show your calculation steps.
"""

import numpy as np


def fermat_factorization(_n):
    a = np.ceil(np.sqrt(_n))
    print(f"a = {a}")
    b = np.sqrt(a ** 2 - _n)
    print(f"b = {b}")
    counter = 0
    print()
    while not b.is_integer():
        counter += 1
        print(f"counter = {counter}")
        if a > b:
            a += 1
            print(f"a = {a}")
            b = np.sqrt(a ** 2 - _n)
            print(f"b = {b}")
            print()
            continue
        else:
            return None, None

    return int(a - b), int(a + b)


if __name__ == "__main__":
    n = 275621053
    print(f"Factorizing n = {n} using Fermat's method.")
    p, q = fermat_factorization(n)

    if p is not None and q is not None:
        print("p = ", p)
        print("q = ", q)
    else:
        print("No factors found in the specified range.")
