n = int(input().strip())
grade = {'Excellent':6, 'Good':4, 'Moderate':3}
update = dict(); maxsal = 0; bestname = list()
for i in range(n):
    real, last, gd, salary = input().strip().split()
    if gd not in grade:
        continue
    else:
        name = real + " " + last
        newsal = int(salary)*grade[gd]
        update[name] = newsal
        if newsal > maxsal:
            bestname = [name]
            maxsal = newsal
        elif newsal == maxsal:
            bestname.append(name)
for j in sorted(bestname):
    print("Name: " + j + ", Bonus: " + str(maxsal))