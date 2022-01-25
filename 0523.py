point = int(input().strip())
alldot = []
for i in range(1, point+1) :
    x, y = [float(e) for e in input().strip().split()]
    listdot = [(x**2 + y **2)**(1/2), i, x, y]
    alldot.append(listdot)
alldot.sort()
print("#" + str(alldot[2][1]) + ": (" + str(alldot[2][2]) + ", " + str(alldot[2][3]) + ")")