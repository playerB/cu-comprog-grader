import math
num = input().split(",")
nine = "9"*len(num[2])
zero = "0"*len(num[1])
downfrac = int(nine + zero)
upfrac = int(num[0] + num[1])*int(nine) + int(num[2])
gcd = math.gcd(upfrac, downfrac)
result = str(int(upfrac//gcd)) + " / " + str(int(downfrac//gcd))
print(result)