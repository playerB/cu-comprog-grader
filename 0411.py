string = input()
i = 0
n = 0
charkeep = [""]*(len(string)-1)
charcount = [0]*(len(string)-1)
result = ""
while i < len(string)-1 :
    if string[i] != string[i+1] :
        charkeep[n] = string[i]
        charcount[n] += 1
        result += charkeep[n] + " " + str(charcount[n]) + " "
        n += 1
        i += 1
    elif string[i] == string[i+1] :
        charcount[n] += 1
        i += 1
if i == len(string)-1 :
    charkeep[n] = string[i]
    charcount[n] += 1
print(result + charkeep[n], charcount[n])