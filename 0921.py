def factor(N):
    fac = list()
    for i in range(2, N):
        if i > N: break
        if N % i == 0:
            f = 0
            while N % i == 0:
                N = N // i
                f += 1
            fac.append([i, f])
    if len(fac) == 0: fac.append([N, 1])
    return fac

exec(input().strip())