"""
Task 3
a) Let n = 1829 and B = 5. Find a prime factor of n by using Pollard (p−1) attack.

https://www.untruth.org/~josh/math/pollard-p-1.pdf

b) Let n = 18779. Using Pollard (p−1), how small B can be used for the attack to be successful
 (Use knowledge of the factorizations of n.) You do not need to find the factorization.

"""

import math


def pollard_p_minus_1(n, B=5):
    a = 2
    for j in range(2, B + 1):
        a = a ** j % n
        d = math.gcd(a - 1, n)
        if 1 < d < n:
            return "Found factor: " + str(d)
    return "No factor found"


def prime_factorization(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return factors


if __name__ == "__main__":
    print("Task 3a:")
    print(pollard_p_minus_1(1829))

    print("\nTask 3b:")

    # Factorize n = 18779 to find its prime factors p and q
    p, q = prime_factorization(18779)

    # Find the largest prime factors of p - 1 and q - 1
    largest_prime_factor_p_minus_1 = max(prime_factorization(p - 1))
    largest_prime_factor_q_minus_1 = max(prime_factorization(q - 1))

    B = min(largest_prime_factor_p_minus_1, largest_prime_factor_q_minus_1)

    # Test and see if attack is successful
    print(pollard_p_minus_1(18779, B))
