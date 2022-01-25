dod = list()
while True:
    order = input().strip().split()
    if len(order) < 5 : break
    number, deliver, d, m, y = order[0], order[1], int(order[2]), int(order[3]), int(order[4])
    a = 0; dtime = {'E':1, 'Q':3, 'N':7, 'F':14}
    if (y-543) % 400 == 0 or ((y-543) % 4 == 0 and (y-543) % 100 != 0): a = 1
    dom = [0, 31, 28 + a, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y < 2558:
        print("Error: " + " ".join(order) + " --> Invalid year")
    elif m < 1 or m > 12:
        print("Error: " + " ".join(order) + " --> Invalid month")
    elif d < 1 or d > dom[m]:
        print("Error: " + " ".join(order) + " --> Invalid date")
    elif deliver not in "EQNF":
        print("Error: " + " ".join(order) + " --> Invalid delivery type")
    else:
        if d + dtime[deliver] > dom[m] and m < 12:
            d = d + dtime[deliver] - dom[m]
            m += 1
        elif d + dtime[deliver] > dom[m] and m == 12:
            d = d + dtime[deliver] - dom[m]
            m = 1
            y += 1
        else:
            d += dtime[deliver]
        dod.append([y, m, d, number])
for i in sorted(dod):
    print(str(i[3]) + ": delivered on " + str(i[2]) + '/' + str(i[1]) + '/' + str(i[0]))