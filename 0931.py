def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_coprime(a, b, c):
    return gcd(gcd(a, b), c) == 1 and gcd(a, gcd(b, c)) == 1 and gcd(gcd(a, c), b) == 1

def primitive_Pythagorean_triples(max_len):
    pPt = list()
    for c in range(2, max_len + 1):
        for b in range(c, 2, -1):
            for a in range(2, b):
                if a**2 + b**2 == c**2 and is_coprime(a, b, c):
                    pPt.append([a, b, c])
    return pPt

exec(input().strip())