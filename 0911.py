n = int(input())
for i in range(n):
    p = 0; newpyt = ''; leftp = True
    pyt = input().strip()
    for j in pyt:
        if j == '.' and leftp :
            p += 1
        else:
            leftp = False
            newpyt += j
    print('.'*(p//2) + newpyt)