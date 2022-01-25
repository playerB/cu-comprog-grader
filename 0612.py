def is_prime(n):
    if n <= 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True

def next_prime(N):
    i = N + 1
    while True:
        if is_prime(i):
            break
        else:
            i += 1
    return i

def next_twin_prime(N):
    i = N + 1
    while True:
        if is_prime(i) and next_prime(i) == i+2:
            return i, i+2
        else:
            i += 1

exec(input().strip())