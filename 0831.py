def total(pocket):
    net = 0
    for money in pocket:
        net += int(money)*int(pocket[money])
    return net

def take(pocket, money_in):
    for money in money_in:
        if money in pocket:
            pocket[money] += money_in[money]
        else:
            pocket[money] = money_in[money]

def pay(pocket, amt):
    temppocket = dict(pocket)       # copy old pocket
    paid = dict()                   # keep track of paid coin
    for i in sorted(list(pocket.keys()), reverse=True): # sort pocket by large coin -> small coin
        if amt - i < 0:             # start new loop for smaller coin
            continue
        elif amt == 0:              # end break
            break
        for j in range(0, pocket[i]):
            if amt - i < 0:         # skip to new loop for smaller coin
                break
            amt -= i                # paid by 1 coin at a time
            paid[i] = j + 1         # keep track of paid coin
        pocket[i] = pocket[i] - paid[i]   # leftover in pocket
    if amt > 0:
        ret = dict()
        pocket.update(temppocket)   # use backed up old pocket
        return ret                  # return empty dict
    else:
        return paid                 # return paid

exec(input().strip())