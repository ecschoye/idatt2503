def a(a, b, n):
    print("Demonstrates that a % n == b % n if and only if a ≡ b (mod n)")
    if is_mod_equal(a, b, n):
        print(f"{a} % {n} == {b} % {n}")
    else:
        print(f"{a} % {n} != {b} % {n}")
    if is_congruent(a, b, n):
        print(f"{a} ≡ {b} (mod {n})")
    else:
        print(f"{a} ≢ {b} (mod {n})")

    if is_congruent(a, b, n) == is_mod_equal(a, b, n) is True:
        print("a % n == b % n if and only if a ≡ b (mod n)")

    print()


def b():
    print("b)")
    print("Calculate the following:")
    print("−99 mod 1001")
    print(mod(-99, 1001))
    """
    -99 mod 1001
    -99 + 1001 = 902
    """
    print()


def c():
    print("c)")
    print("Calculate the following:")
    print("232 + 22 * 77 - 18 ** 3 mod 8")
    print(mod(232 + 22 * 77 - 18 ** 3, 8))
    """
    232 + 22 * 77 - 18 ** 3 mod 8
    232 + 1694 - 5832 mod 8
    -3906 mod 8
    -2 x 1953 mod 8
    -2 x 1 mod 8
    -2 + 8 = 6
    """
    print()


def d():
    print("d)")
    print("Check if 55 ≡ 77 (mod 12)")
    if is_congruent(55, 77, 12):
        print("55 ≡ 77 (mod 12)")
    else:
        print("55 ≢ 77 (mod 12)")


def mod(a, n):
    return a % n


def is_mod_equal(a, b, n):
    return a % n == b % n


def is_congruent(a, b, n):
    return a % n == b % n



if __name__ == "__main__":
    a(55, 77, 12)
    a(15, 3, 1)
    b()
    c()
    d()
