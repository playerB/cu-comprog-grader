n = int(input().strip())
price = dict(); allBidder = dict();successBid = dict(); prio = 0
for i in range(n):
    bid = input().strip().split()
    prio -= 1
    if bid[0] == 'B':
        bidder = bid[1]; biditem = bid[2]; bidprice = int(bid[3])
        d = {bidder: [bidprice, prio]}
        successBid[bidder] = list()
        if biditem not in price:
            price[biditem] = dict(d)
        else:
            price[biditem].update(d)
        allBidder[bidder] = 0
    elif bid[0] == 'W':
        bidder = bid[1]; biditem = bid[2]
        if bidder in allBidder:
            if biditem in price and bidder in price[biditem]:
                price[biditem].pop(bidder)
for i in [[sorted([[bp, bd] for bd, bp in price[k].items()], reverse=True)[:1], k] for k, v in price.items()]:
    if len(i[0]) > 0:
        allBidder[i[0][0][1]] -= i[0][0][0][0]
        if i[0][0][1] in successBid:
            successBid[i[0][0][1]].append(i[1])
for i in sorted(allBidder):
    if len(successBid[i]) != 0:
        buy = ' -> ' + ' '.join(sorted(successBid[i]))
    else: buy = ''
    print(i + ': $' + str(allBidder[i]*(-1)) + buy)