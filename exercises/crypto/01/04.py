"""
Oppgave 4
Du har snappet om følgende melding mellom Alice og Bob: (Her er mellomrom fra klartekst fjernet, og chifferteksten er gruppert med 5 tegn.)
YÆVFB VBVFR ÅVBV
Du vet at Alice og Bob bruker et k-skift-chiffer. Bruk brute-force til å finne krypteringsnøkkelen og klarteksten.
Skriv gjerne et program for å hjelpe deg.
"""

alphabet = "abcdefghijklmnopqrstuvwxyzæøå"


def brute_force_decrypt(text):
    for key in range(len(alphabet)):
        decoded_message = ""
        for char in text:
            if char in alphabet:
                position = alphabet.find(char)
                new_position = (position - key) % len(alphabet)
                new_character = alphabet[new_position]
                decoded_message += new_character
            elif char == " ":
                decoded_message += ""
            else:
                decoded_message += char
        print(f"{decoded_message}")


def a():
    message = "YÆVFB VBVFR ÅVBV".lower()

    brute_force_decrypt(message)
    """
    svar: hjerneneralene
    """


if __name__ == "__main__":
    a()
