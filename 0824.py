def text2keys(text):
    out = ""
    inp = text.lower()
    charli = [" ","abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    for c in inp:
        if "a" <= c <= "z":
            for i in range(len(charli)):
                if c in charli[i]:
                    out += str(i + 1)*(charli[i].find(c) + 1) + " "
        elif c == " ":
            out += "0 "
    return out

def keys2text(keys):
    out = ""
    inp = keys.split()
    charli = [" ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    for c in inp:
        if c != "0":
            out += charli[int(c[0:1]) - 1][len(c)-1:len(c)]
        elif c == "0":
            out += " "
    return out

exec(input().strip())