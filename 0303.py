score = [float(x) for x in input().split()]
score.sort()
res = (score[1] + score[2])/2
print(round(res, 2))