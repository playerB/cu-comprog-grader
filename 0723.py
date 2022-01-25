fname, year = input().strip().split()
fopen = open(fname, 'r')
score = list()
for line in fopen:
    if line[:2] == year[-2:]:
        sid, scr = line.split()
        score.append(float(scr))
if len(score) > 0: print(min(score), max(score), sum(score)/len(score))
else: print('No data')
fopen.close()