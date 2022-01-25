check = 0
num = input()
for i in range(0,12) :
  check += (13-i)*int(num[i])
num12 = (11-(check%11))%10
print(num[0]+" "+num[1:5]+" "+num[5:10]+" "+num[10:12]+" "+str(num12))