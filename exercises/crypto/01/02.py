def a():
    """Display the multiplication table in Z_n (excluding the row or column for 0-times)."""
    print('a)')
    n = 12
    table = mod_multiplication_table(n)
    display_multiplication_table(table)
    print()
    return table


def b(a_results):
    """Which numbers have multiplicative inverses modulo n?"""
    print('b)')
    inverses = get_multiplicative_inverse_mod(a_results)
    display_multiplicative_inverses(inverses)


def c():
    """Do the same for Z11. Which numbers have multiplicative inverses modulo 11?"""
    print('c)')
    z11 = mod_multiplication_table(11)
    inverses = get_multiplicative_inverse_mod(z11)
    display_multiplicative_inverses(inverses)


def d():
    """Find a multiplicative inverse for 11 modulo 29 using brute force."""
    print('d)')
    a = 11
    b = 29
    inv = find_multiplicative_inverse(a, b)
    print(inv)


def display_multiplication_table(table):
    print("   ", end="")
    for i in range(1, len(table) + 1):
        print(f"{i:7}", end="")
    print()
    print("-----------------------------------------------------------------------------------")

    for i, row in enumerate(table):
        print(f"{i + 1:1}", end=" ")
        for val in row:
            print(f"{val:7}", end="")
        print()



def mod_multiplication_table(n):
    return [[(i * j) % n for j in range(1, n)] for i in range(1, n)]


def display_multiplicative_inverses(inverses):
    print(inverses)
    print()


def get_multiplicative_inverse_mod(table):
    return [(i + 1, j + 1) for i, row in enumerate(table) for j, val in enumerate(row) if val == 1]


def find_multiplicative_inverse(a, n):
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    return None


if __name__ == '__main__':
    a_results = a()
    b(a_results)
    c()
    d()
