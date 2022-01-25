string = input()
target = ""
temp = ""
for i in range(0,len(string),1) :
    if string[i] == '[' :
        temp = '('
        target += temp
    elif string[i] == '(' :
        temp = '['
        target += temp
    elif string[i] == ']' :
        temp = ')'
        target += temp
    elif string[i] == ')' :
        temp = ']'
        target += temp
    else :
        temp = string[i]
        target += temp
print(target)
