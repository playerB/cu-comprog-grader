n = int(input().strip())
dr = {}; dn = {}
for i in range(n):
    real, nick = input().strip().split()
    dr[real] = nick
    dn[nick] = real
m = int(input().strip())
for i in range(m):
    inp = input().strip()
    if inp in dr:
        print(dr[inp])
    elif inp in dn:
        print(dn[inp])
    else:
        print('Not Found')