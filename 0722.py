str1 = input().strip().lower()
str2 = input().strip().lower()
newS1 = list(); newS2 = list(); isAnagram = True
for c in str1:
    if c != ' ': newS1.append(c)
for c in str2:
    if c != ' ': newS2.append(c)
if len(newS1) != len(newS2):
    isAnagram = False
for c in newS1:
    try:
        newS2.remove(c)
    except:
        isAnagram = False
if len(newS2) == 0 and isAnagram: print('YES')
else: print('NO')