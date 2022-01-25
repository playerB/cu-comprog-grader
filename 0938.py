station = dict()
travel = set()
while True:
    connect = input().strip().split()
    if len(connect) == 2:
        if connect[0] not in station:
            station[connect[0]] = set()
        if connect[1] not in station:
            station[connect[1]] = set()
        station[connect[0]].add(connect[1])
        station[connect[1]].add(connect[0])
    else:
        while True:
            travel.add(connect[0])
            if connect[0] not in station:
                break
            else:
                for i in station[connect[0]]:
                    travel.add(i)
                    for j in station[i]:
                        travel.add(j)
                break
        break
for i in sorted(travel):
    print(i)