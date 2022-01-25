mobile = input()
if mobile[0] == "0" and mobile[1] in ["6", "8", "9"] and len(mobile) == 10 :
    print("Mobile number")
else :
    print("Not a mobile number")