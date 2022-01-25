rotate = input().strip()
myString = ""; lenRowString = 0; rowLenCheck = []; errorCode = 0
row = int(input().strip())
for i in range(0, row) :
    tempMyString = input().strip()
    myString += tempMyString
    rowLenCheck.append(len(tempMyString))
for j in range(0, len(rowLenCheck)) :
    if len(tempMyString) != rowLenCheck[j] :
        print("Invalid size")
        errorCode = 1
        break
if errorCode == 0 :
    lenRowString = len(myString) // row
    if rotate == '90' :
        for i in range(0, lenRowString) :
            resultString = ""
            for j in range(1, row +1) :
                resultString += myString[len(myString) - (lenRowString * j) + i]
            print(resultString)
    elif rotate == 'flip' :
        for i in range(1, row +1) :
            resultString = ""
            for j in range(1, lenRowString +1) :
                resultString += myString[lenRowString * i -j]
            print(resultString)
    elif rotate == '180' :
        for i in range(0, row) :
            resultString = ""
            for j in range(1, lenRowString +1) :
                resultString += myString[len(myString)- lenRowString*i - j]
            print(resultString)