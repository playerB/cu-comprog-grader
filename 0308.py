d = int(input())
m = int(input())
y = int(input())
a = 0
y -= 543
if y % 400 == 0:
    a = 1
elif y % 4 == 0 and y % 100 != 0 :
    a = 1
monthtoday = [0, 0, 31, 59+a, 90+a, 120+a, 151+a, 181+a, 212+a, 243+a, 273+a, 304+a, 334+a]
d = d + monthtoday[m]
print(d)