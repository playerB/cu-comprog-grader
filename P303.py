fname = input().strip()
myfile = open(fname, 'r'); read = ''
k = int(input())
ruler = ''
for i in range(k // 10):
    ruler += '-'*9 + str(i+1)
if k % 10 != 0:
    ruler += '-'*(k%10)
print(ruler)
for line in myfile:
    if line[-1] == '\n':
        read += line[:-1] + '.'
    else: read += line
n0 = 0; n = 0; j = 0; c = 0
for i in range(len(read)):
    j += 1
    if read[i] == '.' and j <= k + 1:
        n = i
        c = j
        print(n, j)
    if j > k:
        if len(read[n0:n].strip('.')) > 0:
            print(read[n0:n].strip('.'))
        j = k +1-c ; n0 = n
    if i == len(read) -1:
        print(read[n0:].strip('.'))