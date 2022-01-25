fname = input().strip()
file = open(fname, 'r')
cmd = input().strip()
line = file.readline()
p = [i for i in range(len(line))]
while len(line) > 0:
    for j in range(len(line)):
        if line[j] != '.':
            if j in p: p.remove(j)
    line = file.readline()
file.close()
file = open(fname, 'r')
lst = list()
for i in range(len(p)):
    if p[i + 1] - p[i] == 1:
        lst.append(p[i])
        lst.append(p[i+1])
    else: break
rst = list()
for i in range(len(p)-1, 1, -1):
    if p[i - 1] - p[i] == -1:
        rst.append(p[i])
        rst.append(p[i - 1])
    else: break

def mystrip(cmd):
    for line in file:
        newline = ''
        for j in range(len(line)):
            if j not in cmd: newline += line[j]
        print(newline)

if cmd == 'LSTRIP':
    mystrip(lst)
elif cmd == 'RSTRIP':
    mystrip(rst)
elif cmd == 'STRIP':
    mystrip(lst + rst)
elif cmd == 'STRIP_ALL':
    mystrip(p)
else: print('Invalid command')
file.close()