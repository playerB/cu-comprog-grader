import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    sid = data[:, 0].tolist(); lower_avg = list()
    wt = np.append(np.zeros(1), weight, axis=0).reshape((4, 1))
    total = data.dot(wt).T
    avg = np.mean(total)
    for i in range(len(total[0])):
        if (total < avg).tolist()[0][i] : lower_avg.append(str(sid[i]))
    if len(lower_avg) > 0: print(', '.join(lower_avg))
    else: print('None')

exec(input().strip())