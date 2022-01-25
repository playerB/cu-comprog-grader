numCount = 0
totalSum = 0
while True :
    numInput = input()
    if numInput == 'q' :
        break
    else :
        numInput = float(numInput)
        totalSum += numInput
        numCount += 1
if numCount == 0 :
    print("No Data")
else :
    avg = totalSum/numCount
    print(round(avg,2))
