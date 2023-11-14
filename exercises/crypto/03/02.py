def HMAC(message):
    key = 0b1001
    ipad = 0b0011
    opad = 0b0101

    # h is the midsqare-hashing
    h = ((message * message) & 0b1111111) >> 3 & 0b1110
    print(f"Square of the message: {h:04b}")


if __name__ == "__main__":
    # task_1a()
    # task_1b()
    HMAC(0b1011)