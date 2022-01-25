f = input().split()
data = []
peak = 0
for i in range(0, len(f)) :
    data.append(float(f[i]))
for j in range(1,len(data)-1) :
    if data[j-1] < data[j] :
        if data[j] > data[j+1] :
            peak += 1
print(peak)