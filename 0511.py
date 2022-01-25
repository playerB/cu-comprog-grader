n = str(input())
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
allnum = ""
for i in range(0,10) :
    if n.find(number[i]) > -1 :
        number[i] = "*"
for j in range(0,10) :
    if number[j] != "*" :
        allnum += number[j] + ","
if number.count("*") < 10 :
    print(allnum[:-1])
if number.count("*") == 10 :
    print("None")