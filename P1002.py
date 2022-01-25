n, k = [int(e) for e in input().split()]
if n % 2 != 0 :
    sum_a = 0
    sum_b = 0
    sum_c = 0
    m = 0
    while True :
        if m < k :
            a, b, c = [int(e) for e in input().split()]
            if a == b :
                if b == c :
                    if (a+b) > k :
                        sum_a += 1
                        sum_b += 2
                        sum_c -= 3
                    else:
                        sum_a -= 3
                        sum_b -= 2
                        sum_c += 1
                else:
                    sum_a += 2
                    sum_b -= 3
            m += 1
        else:
            print(sum_a, sum_b, sum_c)
            break
else:
    s, t = [int(e) for e in input().split()]
    x, y = s, t
    if s > t:
        x = s - t
    elif s < t :
        y = 2*(t - s)
    if (x + y) > k :
        x, y = y, x
        x = y + s*s
    print(x, y)