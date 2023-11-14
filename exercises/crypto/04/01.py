"""
Task 1
Factorize n = 275621053.
You can assume that n = pq, where p−q is relatively small.
Show your calculation steps.
"""

import numpy as np

def factorize(n):
    sqrt_n = np.sqrt(n)
    sqrt_n_int = int(sqrt_n)
    search_range = 1000000

    for i in range(sqrt_n_int, sqrt_n_int - search_range, -1):
        if n % i == 0:
            _p = i
            _q = n // i
            return _p, _q

    return None, None

if __name__ == "__main__":
    n = 275621053
    p, q = factorize(n)

    if p is not None and q is not None:
        print("p = ", p)
        print("q = ", q)
    else:
        print("No factors found in the specified range.")
