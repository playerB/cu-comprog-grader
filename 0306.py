weight = int(input())
price = 0
if weight <= 100 :
    price = 18
elif 100 < weight <= 250 :
    price = 22
elif 250 < weight <= 500 :
    price = 28
elif 500 < weight <= 1000 :
    price = 38
elif 1000 < weight <= 2000 :
    price = 58
if weight > 2000 :
    print("Reject")
elif weight <= 2000 :
    print(price)
