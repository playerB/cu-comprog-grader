import math
bd, bm, by, d, m, y = [int(e) for e in input().strip().split()]
a = 0
by -= 543
y -= 543
if (by % 400 == 0 or (by % 4 == 0 and by % 100 != 0)) and (bm <= 2 and bd <= 28):
    a += 1
if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)) and m >= 3:
    a += 1
motod = [0, 31, 28+a, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if y - by > 1 :
    day = sum(motod[bm:13]) + sum(motod[0:m]) + (y - by -1)*365 - bd + d
else :
    day = sum(motod[bm:13]) + sum(motod[0:m]) - bd + d
print(day, "{:.2f}".format(math.sin(2*math.pi*day/23)), "{:.2f}".format(math.sin(2*math.pi*day/28)), "{:.2f}".format(math.sin(2*math.pi*day/33)))