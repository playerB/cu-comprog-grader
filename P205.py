string1 = input().strip()
string2 = input().strip()
s1 = [e for e in string1.lower() if 'a' <= e <= 'z']
s2 = [e for e in string2.lower() if 'a' <= e <= 'z']
for c in s1 + s2:
    if c in s1 and c in s2:
        s1.remove(c)
        s2.remove(c)
print(string1)
if len(set(s1)) == 0:
    print("- None")
for i in sorted(set(s1)):
    if s1.count(i) > 1:
        print("- remove " + str(s1.count(i)) + ' ' + i + "'s")
    else:
        print("- remove " + str(s1.count(i)) + ' ' + i)
print(string2)
if len(set(s2)) == 0:
    print("- None")
for i in sorted(set(s2)):
    if s2.count(i) > 1:
        print("- remove " + str(s2.count(i)) + ' ' + i + "'s")
    else:
        print("- remove " + str(s2.count(i)) + ' ' + i)