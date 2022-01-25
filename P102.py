mode = input().strip()
if mode == "str2RLE" :
    string = input().strip()
    i = 0
    n = 0
    charkeep = [""] * (len(string) - 1)
    charcount = [0] * (len(string) - 1)
    result = ""
    while i < len(string) - 1:
        if string[i] != string[i + 1]:
            charkeep[n] = string[i]
            charcount[n] += 1
            result += charkeep[n] + " " + str(charcount[n]) + " "
            n += 1
            i += 1
        elif string[i] == string[i + 1]:
            charcount[n] += 1
            i += 1
    if i == len(string) - 1 and len(string) > 1:
        charkeep[n] = string[i]
        charcount[n] += 1
    if len(string) > 1 :
        print(result + charkeep[n], charcount[n])
    elif len(string) == 1:
        print(string, 1)
elif mode == "RLE2str" :
    rle = input().strip().split()
    result = ""
    for i in range(len(rle)) :
        if i % 2 == 0 :
            char = rle[i]
        elif i % 2 == 1 :
            result += char*int(rle[i])
    print(result)
else:
    print("Error")