n = int(input())
k = int(input())
if n >= 0 and k >= 1:
    out = ''
    for i in range(1, k + 1):
        if i <= k-1: m = n + 1
        else: m = n
        out += str(i) + '-' * (m - len(str(i)))
    print(out)
    gc = ['0', '1']
    for i in range(n - 1):
        for e in gc[::-1]:
            gc.append(e)
        for j in range(len(gc) // 2):
            gc[j] = '0' + gc[j]
        for j in range(len(gc) // 2, len(gc)):
            gc[j] = '1' + gc[j]
    for i in range(len(gc) // k + 1):
        print(','.join(gc[k * i: k * (i + 1)]))
elif n < 0 and k >= 1: print('Invalid n')
elif n >= 0 and k < 1: print('Invalid k')
else: print('Invalid n and k')