while True:
    string = input().strip()
    if string == 'end': break
    rot13 = ''
    for c in string:
        if 'A' <= c < 'N': rot13 += chr(ord(c) + 13)
        elif 'N' <= c <= 'Z': rot13 += chr(ord(c) - 13)
        elif 'a' <= c < 'n': rot13 += chr(ord(c) + 13)
        elif 'n' <= c <= 'z': rot13 += chr(ord(c) - 13)
        else:
            rot13 += c
    print(rot13)