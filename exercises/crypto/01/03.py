"""

Vi skal bruke alfabetet a-å (kun små bokstaver) for klartekst, og skriver chiffer-tekst med store bokstaver. Vi identifiserer også bokstavene med tallene fra 0 til 28, betraktet som tall i Z29, dvs. heltallene modulo 29.
Vi har en funksjon f : Z29 → Z29 til gitt ved formelen
f(x)=(11·x−5) mod29
"""

alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

def f(x):
    return (11 * x - 5) % len(alphabet)

def f_inverse(y):
    return (8 * y + 11) % len(alphabet)

def a():
    print("a)")
    char_list = []

    for i in range(len(alphabet)):
        char_list.append(f(i))
    for i in range(len(alphabet)):
        print(f"{alphabet[i]}: {char_list[i]}")

    print()

def c():
    """
    Finn den inverse permutasjonen f−1 til f, både
        – som en sekvens av verdier f−1(0),f−1(1),...
        – som formel på formen f^−1(y)=ay+b(mod29),dvs.bestem a og b.
    """
    print("c)")
    for i in range(len(alphabet)):
        print(f"{alphabet[i]}: {f_inverse(i)}")
    print()

def d():
    """
     Bruk f som nøkkel i et enkelt substitusjons-chiffer til å kryptere meldingen m = ’alice’
    """
    message = "alice"
    encoded_message = ""
    for char in message:
        char_index = alphabet.find(char)
        encoded_char_index = f(char_index)
        encoded_char = alphabet[encoded_char_index]
        encoded_message += encoded_char
    print(encoded_message)
    print()


def e():
    """
    Bruk f som nøkkel og dekrypter c = SIØPBE
    """
    print("e)")
    encoded_message = "SIØPBE"
    decoded_message = ""
    for char in encoded_message.lower():
        char_index = alphabet.find(char)
        decoded_char_index = f_inverse(char_index)
        decoded_char = alphabet[decoded_char_index]
        decoded_message += decoded_char
    print(decoded_message)

if __name__ == "__main__":
    a()
    c()
    d()
    e()
