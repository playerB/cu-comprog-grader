import math
par = []; stroke = []; strokeFix = []
for i in range(9) :
    p, s, c = [int(e) for e in input().strip().split()]
    par.append(p)
    stroke.append(s)
    if c == 1 :
        strokeFix.append(min(p+2, s))
    else:
        strokeFix.append(0)
extraPts = math.floor(0.8*(1.5*sum(strokeFix)-sum(par)))
total = sum(stroke)-extraPts
print(sum(stroke))
print(extraPts)
print(total)