num1, num2 = [int(x, 2) for x in input().strip().split()]
num1 += num2
print(bin(num1)[2:])