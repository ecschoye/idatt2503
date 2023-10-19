# Krypto 01

## Oppgave 2

### e)
Formuler en sammenheng mellom det at a har en multiplikativ invers modulo n, og om tallet har felles faktorer med n.

Hvis a har en multiplikativ invers modulo n, så har a og n ingen felles faktorer.

## Oppgave 3

### b) Forklar at f er en permutasjon av Z_29.

En permutasjon av en mengde Z er en bijeksjon fra Z til Z.
Det er altså en avbildning Φ: Z -> Z som er både injektiv og surjektiv, og har derfor også en invers avbildning.

En funksjon f: X -> Y er surjektiv hvis for alle y i Y, finnes det et x i X slik at f(x) = y.

For å vise at f er surjektiv må vi vise at for alle y i Y, finnes det et x i X slik at f(x) = y.
Siden f(x) er lineær, så er f(x) = a*x <=> y = a*x.

En funksjon f: X -> Y er injektiv hvis for alle x1, x2 i X, hvis f(x1) = f(x2), så er x1 = x2.
For å vise at f er injektiv må vi vise at f(x1) = f(x2) => x1 = x2.
Siden f(x) er lineær, så er f(x1) = f(x2) <=> a*x1 = a*x2 <=> x1 = x2.

Siden f er både injektiv og surjektiv, er den en bijektiv funksjon og dermed en permutasjon av Z29.


## Oppgave 5

### c) Hvis nøkkelordet har lengde 15, hvor mange nøkler finnes? Vil du anse dette som sikkret med tanke på et brute-force angrep?

Det finnes 29^15 mulige nøkler. 
Det er 29 mulige bokstaver i alfabetet, og 15 mulige plasser i nøkkelen.