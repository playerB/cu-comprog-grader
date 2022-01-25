x = input().strip()
y = x + '$'
table = list()
bwt = ""
for i in range(len(y)):
    shift = y[i:] + y[:i]
    table.append(shift)
table.sort()
for j in table:
    bwt += j[-1]
print(bwt)