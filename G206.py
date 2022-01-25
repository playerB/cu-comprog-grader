c1 = int(input().strip())
pizzacal = {'PZ871':265.25, 'PZ953':246.50, 'Z1983':256.50, 'Z2853':272.50, 'LC673':309.25}
customer = dict()
for i in range(c1):
    order = [e for e in input().strip().split(',')]
    if order[0] not in customer:
        totalcal = 0
        for j in range(1, len(order) - 1, 2):
            totalcal += pizzacal[order[j]] * int(order[j+1])
        customer[order[0]] = totalcal
    elif order[0] in customer:
        totalcal = 0
        for j in range(1, len(order) - 1, 2):
            totalcal += pizzacal[order[j]] * int(order[j + 1])
        customer[order[0]] += totalcal
for c in sorted(customer):
    print(c + ' -> ' + str(customer[c]))