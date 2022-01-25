code = input()
decode1 = code[3::7]
decode2 = code[7::5]
decode3 = int(decode1) + int(decode2) + 10000
decode4 = decode3//10%1000
decode5 = decode4//100 + decode4//10%10 + decode4%10
decode6 = decode5%10 +1
decode7 = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
decode8 = decode7[decode6]
final = str(decode4) + decode8
print(final)