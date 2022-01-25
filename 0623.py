def make_int_list(x):
    return [int(n) for n in x.strip().split()]

def is_odd(e):
    return e%2 == 1

def odd_list(alist):
    oddli = []
    for li in alist:
        if is_odd(li):
            oddli.append(li)
    return oddli

def sum_square(alist):
    tli = []
    for li in alist:
        li *= li
        tli.append(li)
    return sum(tli)

exec(input().strip())