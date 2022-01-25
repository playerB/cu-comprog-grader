word = input().strip()
newword = ''; c = 0; skip = False
while c < len(word):
    if 'a' <= word[c] <= 'z' or 'A' <= word[c] <= 'Z' or '0' <= word[c] <= '9':
        if skip:
            newword += word[c].upper()
        else:
            newword += word[c].lower()
        skip = False
        c += 1
    else:
        skip = True
        c += 1
print(newword[0].lower() + newword[1:])