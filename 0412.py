row = int(input())
x = []
y = []
aList = []
bList = []
for i in range(1,row+1) :
    string = input()
    substr = string.split( )
    x.insert(i, int(substr[0]))
    y.insert(i, int(substr[1]))
zz = input()
for j in range(1,row,2) :
    aList.append(x[j])
for k in range(0,row,2) :
    aList.append(y[k])
for j in range(0,row,2) :
    bList.append(x[j])
for k in range(1,row,2) :
    bList.append(y[k])
print(list(aList), list(bList))
if zz == "Zig-Zag" :
    print(min(bList), max(aList))
elif zz == "Zag-Zig" :
    print(min(aList), max(bList))
