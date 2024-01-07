"""
Alice and Bob want to have an common key using Diffie-Hellmann key exchange.
They agree on using the prime 101, and base n = 3.
Alice choosed her secret a = 33, and Bob chooses b = 65.

a)  Write a program that prints out all the powers 3**i for i = 1,...,100.
    Do the same for 5**i. What is a major difference between these two sequences?

b) Find their common key.

"""


def powers(base, _range):
    for i in range(1, _range + 1):
        yield base ** i % 101


def find_common_key(_p=101, _n=3, _a=33, _b=65):
    a_1 = _n ** _a % _p
    b_1 = _n ** _b % _p
    k_1 = a_1 ** _b % _p
    k_2 = b_1 ** _a % _p
    if k_1 == k_2:
        return k_1
    else:
        return None


if __name__ == "__main__":
    print("Task 4a:")
    print("Powers of 3:")
    print(list(powers(3, 100)))
    print("Powers of 5:")
    print(list(powers(5, 100)))
    print("\nThe difference i notice is that the powers of 5 increment at a much faster rate than the powers of 3.")

    print("\nTask 4b:")
    print("Common key: ", find_common_key())
