allframe = input().strip()
askframe = int(input().strip())
framescore = []; realscore = []; total = 0; x = 0
for i in range(len(allframe)) :
    if allframe[i] == 'X' :
        framescore.append(10)
    elif allframe[i] == '/' :
        framescore.append(10-int(allframe[i-1]))
    else:
        framescore.append(int(allframe[i]))
for j in range(len(framescore)-1) :
    if framescore[j] == 10 :
        if j < len(framescore)-2 :
            realscore.append(10+framescore[j+1]+framescore[j+2])
        x += 1
    elif framescore[j]+framescore[j+1] == 10 and allframe[j+1] == '/':
        if j < len(framescore)-2:
            realscore.append(10+framescore[j+2])
    elif x % 2 == 1 and j % 2 == 0 and framescore[j] < 10 :
        continue
    elif x % 2 == 0 and j % 2 == 1 and framescore[j] < 10 :
        continue
    else:
        if allframe[j] != '/' and allframe[j] != 'X':
            realscore.append(framescore[j]+framescore[j+1])
for k in range(len(realscore)) :
    total += realscore[k]
if 1 <= askframe <= 10 :
#   print(realscore)
    print(realscore[askframe-1])
else:
    print(total)