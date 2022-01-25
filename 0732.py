pw = input().strip()
if len(pw) < 8: print("Less than 8 characters")
lc ,uc ,nb ,sy ,rep ,ornum, orlet, orkey = False, False, False, False, False, False, False, False
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; number =  "01234567890"; symbol = "!@#$%^&*()_+-=[]{};',.\\/" + '"'
for c in pw:
    if c in char.lower(): lc = True
    if c in char: uc = True
    if c in number: nb = True
    if c in symbol: sy = True
for i in range(len(pw)):
    if len(pw[i:i+4]) == 4:
        if pw[i:i+1] == pw[i+1:i+2] == pw[i+2:i+3] == pw[i+3:i+4]: rep = True
        if pw[i:i+4] in number + number[::-1]: ornum = True
        if pw[i:i+4].upper() in char + char[::-1]: orlet = True
        if pw[i:i+4] in symbol + symbol[::-1] or pw[i:i+4].lower() in "qwertyuiopoiuytrewq" or pw[i:i+4].lower() in "asdfghjklkjhgfdsa" or pw[i:i+4].lower() in "zxcvbnmnbvcxz": orkey = True
if not lc : print("No lowercase letters")
if not uc : print("No uppercase letters")
if not nb : print("No numbers")
if not sy : print("No symbols")
if rep: print("Character repetition")
if ornum: print("Number sequence")
if orlet: print("Letter sequence")
if orkey: print("Keyboard pattern")
if lc and uc and nb and sy and not rep and not ornum and not orlet and not orkey: print("OK")
