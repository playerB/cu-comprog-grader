allcard = input().strip().split()
cutnshuf = input().strip()
half = len(allcard)//2
for i in range(len(cutnshuf)) :
    if cutnshuf[i] == 'C' :
        allcard = allcard[half:len(allcard)] + allcard[0:half]
    elif cutnshuf[i] == 'S' :
        tempAllcard = []
        for j in range(0, half) :
            tempAllcard.append(allcard[0+j])
            tempAllcard.append(allcard[half+j])
        allcard = tempAllcard
    else:
        continue
print(" ".join(allcard))