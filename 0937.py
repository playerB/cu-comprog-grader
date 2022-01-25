n = int(input())
dep = dict(); stu = dict(); choose = dict()
for i in range(n):
    department, amt = input().strip().split()
    dep[department] = int(amt)
m = int(input())
for i in range(m):
    sid, score, d1, d2, d3, d4 = input().strip().split()
    stu[sid] = [float(score), d1, d2, d3, d4]
for s in sorted([[v, k] for k, v in stu.items()], reverse=True):
    for i in range(1, 5):
        if dep[s[0][i]] > 0:
            choose[s[1]] = s[0][i]
            dep[s[0][i]] -= 1
            break
        elif dep[s[0][i]] == 0:
            i += 1
for i in sorted(choose.keys()):
    print(i, choose[i])