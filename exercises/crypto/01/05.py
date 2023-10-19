alphabet = "abcdefghijklmnopqrstuvwxyzæøå"


def encrypt(message, key):
    encoded_message = ""
    key_index = 0
    for char in message:
        if char in alphabet:
            char_index = alphabet.find(char)
            key_char_index = alphabet.find(key[key_index % len(key)])
            encoded_char_index = (char_index + key_char_index) % len(alphabet)
            encoded_char = alphabet[encoded_char_index]
            encoded_message += encoded_char
            key_index += 1
        else:
            encoded_message += char
    return encoded_message

def decrypt(message, key):
    decoded_message = ""
    key_index = 0
    for char in message:
        if char in alphabet:
            char_index = alphabet.find(char)
            key_char_index = alphabet.find(key[key_index % len(key)])
            decoded_char_index = (char_index - key_char_index) % len(alphabet)
            decoded_char = alphabet[decoded_char_index]
            decoded_message += decoded_char
            key_index += 1
        else:
            decoded_message += char
    return decoded_message


def a():
    print("a)")
    key = "torsk"
    message = "Snart helg".lower()
    print(encrypt(message, key))
    print()

def b():
    print("b)")
    key = "brus"
    encoded_message = "QZQOBVCAFFKSDC".lower()
    print(decrypt(encoded_message, key))
    print()



if __name__ == "__main__":
    a()
    b()

