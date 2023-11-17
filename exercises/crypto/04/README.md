# Task 2

## a ) 

n_1 =  1676881
n_1 factorized: 1283 * 1307 = 1676881
Number of iterations: 0

n_2 =  2410757
n_2 factorized: 1283 * 1879 = 2410757
Number of iterations: 28

n_3 =  2569849
n_3 factorized: 1283 * 2003 = 2569849
Number of iterations: 39

n_4 =  2600641
n_4 factorized: 1283 * 2027 = 2600641
Number of iterations: 42

By factorizing with Fermat's method we see that q_4 = 2027 is the best choice for q given p = 1283. 
This is because it took the most number of iterations to factorize n given q.


# Task 4

## a)

Show that encryption in RSA has the following property:

e_K(x_1) * e_K(x_2) mod n = e_K(x_1 * x_2) mod n

### Proof

Given that RSA encryption for message x is e_K(x) = x^e mod n,
where e is the public exponent and n is the modulus.

For x_1:
e_K(x_1) = x_1^e mod n

For x_2:
e_K(x_2) = x_2^e mod n

For x_1 * x_2:
e_K(x_1 * x_2) = (x_1 * x_2)^e mod n

LHS = e_K(x_1) * e_K(x_2) mod n = (x_1^e mod n) * (x_2^e mod n) mod n = ((x_1^e * x_2)^e mod n) mod n

RHS = e_K(x_1 * x_2) mod n = ((x_1 * x_2)^e mod n) mod n 

LHS = RHS

## b)

Show how RSA is vulnerable to chosen cipher text attack: For ciphertext `y`, 
then Eva can choose some `r ≢ 1 (mod n)`, and construct `y' = y * r^e`. 
If she then knows the decryption `x' = d_K(y')`, show how she can calculate `x = d_K(y)`. 
(Hint: She can also calculate r−1 mod n)

Chosen cipher text y'
y' = y * r^e 
y' ≡ y * r^e mod n

Decryption of y'
x' ≡ y'^d mod n

x' ≡ (y * r^e)^d mod n

Application of RSA 
de ≡ 1 (mod φ(n))

r^(ed) ≡ r (mod n)

x' ≡ (y^d * r^ed) mod n

Original message x

x ≡ y^d mod n

x' ≡ y^d * r mod n

Multiply both sides by r^-1 mod n

x' * r^-1 ≡ x mod n

x ≡ x' * r^-1 mod n

