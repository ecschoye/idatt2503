def lfsr(recursive_sequence, key):
    initial_value = key
    period = 0
    state = key

    while True:
        new_state = recursive_sequence(state)

        period += 1

        state = new_state

        if new_state == initial_value:
            break

    return period


def lfsr_a(key):
    fourth_bit = (key >> 3) & 1
    third_bit = (key >> 2) & 1
    second_bit = (key >> 1) & 1
    first_bit = key & 1
    # print(f"first bit: {first_bit}, third bit: {third_bit}")
    new_bit = (first_bit + second_bit + third_bit + fourth_bit) % 2
    original_part = key >> 1
    new_key = (new_bit << 3) | original_part
    print(format(new_key, '04b'))
    return new_key


def lfsr_b(key):
    first_bit = key & 1
    fourth_bit = (key >> 3) & 1
    new_bit = (first_bit + fourth_bit) % 2
    original_part = key >> 1
    new_key = (new_bit << 3) | original_part
    print(format(new_key, '04b'))
    return new_key


def task_a(_K1, _K2, _K3):
    print(format(_K1, '04b'))
    print("-----")
    lf = lfsr(lfsr_a, _K1)
    print(f"Period of K1 is {lf}")
    print()
    print(format(_K2, '04b'))
    print("-----")
    lf_2 = lfsr(lfsr_a, _K2)
    print(f"Period of K2 is {lf_2}")
    print()
    print(format(_K3, '04b'))
    print("-----")
    lf_3 = lfsr(lfsr_a, _K3)
    print(f"Period of K3 is {lf_3}")


def task_b(_K1, _K2, _K3):
    print(format(_K1, '04b'))
    print("-----")
    lf = lfsr(lfsr_b, _K1)
    print(f"Period of K1 is {lf}")
    print()
    print(format(_K2, '04b'))
    print("-----")
    lf_2 = lfsr(lfsr_b, _K2)
    print(f"Period of K2 is {lf_2}")
    print()
    print(format(_K3, '04b'))
    print("-----")
    lf_3 = lfsr(lfsr_b, _K3)
    print(f"Period of K3 is {lf_3}")


if __name__ == '__main__':
    K1 = 0b1000
    K2 = 0b0011
    K3 = 0b0101
    print("Task A")
    task_a(K1, K2, K3)
    print()
    print("Task B")
    task_b(K1, K2, K3)
