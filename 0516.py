n = int(input())
result = []
a = []
ans = ''
result.append(n)
while n != 1 :
    if n % 2 == 0 :
        n = n / 2
        result.append(int(n))
    elif n % 2 == 1 :
        n = n * 3 + 1
        result.append(int(n))
result = result[-15:-1]
for i in range(0,len(result)) :
    ans = ans + str(result[i]) + "->"
ans = ans + "1"
print(ans)