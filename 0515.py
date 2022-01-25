n = input().split()
data = []
result = []
for i in range(0,len(n)) :
    data.append(int(n[i]))
data.sort()
result.append(data[0])
for j in range(0,len(data)-1) :
    if data[j] != data[j+1] :
        result.append(data[j+1])
print(len(result))
print(result[:10])
