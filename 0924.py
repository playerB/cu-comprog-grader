animals = dict(); typeorder = list()
while True:
    n = input().strip().split(',')
    if n == ['q']: break
    name = n[0]; type = n[1]
    if type not in animals:
        animals[type] = [name]
        typeorder.append(type)
    else: animals[type].append(name)
for i in typeorder:
    print(i + ': ' + ', '.join(animals[i]))