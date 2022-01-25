def reverse(d):
    dr = {}
    for key in d:
        dr[d[key]] = key
    return dr

def keys(d, v):
    dk = []
    for key in d:
        if d[key] == v :
            dk.append(key)
    return dk

exec(input().strip())