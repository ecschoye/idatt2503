def calculate_lfsr_period(initial_state):
    if initial_state == 0:
        return 0

    bit = initial_state
    period = 0
    while True:
        first_bit = (bit >> 3) & 1
        second_bit = (bit >> 2) & 1
        third_bit = (bit >> 1) & 1
        fourth_bit = bit & 1

        new_bit = first_bit ^ second_bit ^ third_bit ^ fourth_bit

        bit = (bit >> 1) | (new_bit << 3)
        period += 1

        if bit == initial_state:
            break

    return period

def calculate_second_lfsr_period(initial_state):
    if initial_state == 0:
        return 0

    bit = initial_state
    period = 0
    while True:
        first_bit = (bit >> 3) & 1
        fourth_bit = bit & 1
        new_bit = first_bit ^ fourth_bit
        bit = (bit >> 1) | (new_bit << 3)
        period += 1

        if bit == initial_state:
            break

    return period

def task_1a():
    print("Task 1a")
    K_1 = 0b1000
    K_2 = 0b0011
    K_3 = 0b1111
    print("K_1: ", calculate_lfsr_period(K_1))
    print("K_2: ", calculate_lfsr_period(K_2))
    print("K_3: ", calculate_lfsr_period(K_3))

def task_1b():
    print("Task 1b")
    K_1 = 0b1011
    K_2 = 0b0011
    K_3 = 0b1111
    print("K_1: ", calculate_second_lfsr_period(K_1))
    print("K_2: ", calculate_second_lfsr_period(K_2))
    print("K_3: ", calculate_second_lfsr_period(K_3))



if __name__ == "__main__":
    task_1a()
    task_1b()

