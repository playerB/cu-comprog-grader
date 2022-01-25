word = input()
string = input()
wordcount = 0
newString = ""
for c in range(0, len(string)) :
    removePunc = ["'", '"', ',', '.', '(', ')']
    if string[c] not in removePunc :
        newString += string[c]
    if string[c] in removePunc :
        newString += " "
newString = newString.split()
for i in range(0, len(newString)) :
    if newString[i] == word :
        wordcount += 1
print(wordcount)