h = int(input())
print(" "*(h-1) + "*")
for i in range(h-2) :
    print(" "*(h-i-2) + "*" + " "*(i*2+1) + "*")
print("*"*(h*2-1))