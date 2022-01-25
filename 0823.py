n1 = int(input().strip())
tele = dict(); numb = dict(); ans = list()
for i in range(n1):
    realname, lastname, number = input().strip().split()
    name = realname + " " + lastname
    tele[name] = number
    numb[number] = name
n2 = int(input().strip())
for i in range(n2):
    ask = input().strip()
    if ask in tele:
        ans.append([ask, tele[ask]])
    elif ask in numb:
        ans.append([ask, numb[ask]])
    else:
        ans.append([ask, "Not found"])
for i in range(len(ans)):
    print(ans[i][0] + " --> " + ans[i][1])