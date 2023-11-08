def midsquare_hashing(message):
    message_squared = (message * message) % 2 ** 8

    message_squared_binary = bin(message_squared)[2:]

    hash_length = 4
    middle_start = int((len(message_squared_binary) - hash_length) / 2)
    middle_end = int((len(message_squared_binary) + hash_length) / 2)
    hash_result = message_squared_binary[middle_start:middle_end]
    return int(hash_result, 2)


def hmac(K, x):
    ipad = 0b0011
    opad = 0b0101

    return midsquare_hashing((K ^ opad) + midsquare_hashing((K ^ ipad) + x))


if __name__ == '__main__':
    print("2a")
    K = 0b1001
    m = 0b0110
    print(f"HMAC of {format(m, '04b')} with key {format(K, '04b')} is {format(hmac(K,m), '04b')}")
    print()

    print("2b")
    received_message = 0b0111
    received_hmac = 0b0100
    print(f"Received message {format(received_message, '04b')} with HMAC {format(received_hmac, '04b')}")
    print(f"if {format(hmac(K, received_message), '04b')} == {format(received_hmac, '04b')}:")
    if hmac(K, received_message) == received_hmac:
        print("Message is authentic!")
    else:
        print("Message is not authentic!")
