DNA = input().strip().upper()
op = input().strip()
inv = False; rev = ''; a, t, c, g = 0, 0, 0, 0
for p in DNA:
    if p not in 'ATCG':
        print('Invalid DNA')
        inv = True
        break
    if p == 'A': rev += 'T'; a += 1
    elif p == 'T': rev += 'A'; t += 1
    elif p == 'C': rev += 'G'; c += 1
    else: rev += 'C'; g += 1
if not inv:
    if op == 'R':
        print(rev[::-1])
    elif op == 'F':
        print('A=' + str(a) + ', T=' + str(t) + ', G=' + str(g) + ', C=' + str(c))
    elif op == 'D':
        pair = input().strip(); k = 0; n = 0
        while DNA.find(pair, k) > -1:
            if pair in DNA[k:]:
                k = DNA.find(pair, k) +1
                n += 1
        print(n)