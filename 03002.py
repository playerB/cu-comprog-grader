d, m, y = [int(x) for x in input().split()]
y -= 543
n = 31
if m == 4 or m == 6 or m == 9 or m == 11 :
    n = 30
elif m == 2 :
    n = 28
    if (y % 400) == 0 :
        n = 29
    if (y % 4) == 0 and (y % 100) != 0 :
        n = 29
d += 15
if d > n :
    d = d - n
    m += 1
if m > 12 :
    m -= 12
    y += 1
y += 543
print(str(d) + "/" + str(m) + "/" + str(y))