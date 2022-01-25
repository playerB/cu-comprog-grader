t = int(input().strip())
if t == 1:
    s1 = [int(e) for e in input().strip()[1:-1].split(',')]
    s2 = [int(e) for e in input().strip()[1:-1].split(',')]
    dot = list('0'*len(s1))
    for i in range(len(s1)):
        dot[i] = s1[i]*s2[i]
    print(sum(dot))
elif t == 2:
    name = dict()
    numb = dict()
    n1 = int(input().strip())
    for i in range(n1):
        real, last, numb1 = input().strip().split()
        name1 = real + ' ' + last
        name[name1] = numb1
        numb[numb1] = name1
    n2 = int(input().strip())
    ans = list()
    for j in range(n2):
        ask = input().strip()
        if ask in name:
            ans.append(name[ask])
        elif ask in numb:
            ans.append(numb[ask])
        else:
            ans.append('Not found')
    for k in ans:
        print(k)
else:
    p = int(input())
    win = list(); lose = list()
    for i in range(p):
        w, l = input().strip().split()
        if w in lose:
            lose.pop(lose.index(w))
        elif l in win:
            win.pop(win.index(l))
    print()