n = int(input())
win = set(); lose =set()
for i in range(n):
    w, l = input().split()
    win.add(w)
    lose.add(l)
print(sorted(win-lose))