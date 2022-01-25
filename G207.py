string1 = input().strip()
string2 = input().strip()
maxcount1 = 0;maxcount2 = 0; shi1 = 0; shi2 = 0
for i in range(max(len(string1), len(string2))):
    shift = "-"*i
    stringsh1 = shift + string1
    count = 0
    for i1 in range(min(len(stringsh1), len(string2))):
        if stringsh1[i1] == string2[i1]:
            count += 1
    if count > maxcount1:
        maxcount1 = count
        shi1 = i
for j in range(max(len(string1), len(string2))):
    shift = "-"*j
    stringsh2 = shift + string2
    count = 0
    for i2 in range(min(len(string1), len(stringsh2))):
        if string1[i2] == stringsh2[i2]:
            count += 1
    if count > maxcount2:
        maxcount2 = count
        shi2 = j
if maxcount1 >= maxcount2:
    print("-" * int(shi1) + string1)
    print(string2)
    print(int(maxcount1))
elif maxcount2 > maxcount1:
    print(string1)
    print("-" * int(shi2) + string2)
    print(int(maxcount2))