n1 = int(input().strip())
icc = dict(); iccsale = dict(); maxsale = 0; topsale = list()
for i in range(n1) :
    iccname, iccprice = input().strip().split()
    icc[iccname] = int(iccprice)
n2 = int(input().strip())
for i in range(n2) :
    itemname, saleamt = input().strip().split()
    if itemname in icc:
        if itemname not in iccsale:
            iccsale[itemname] = icc[itemname] * int(saleamt)
        else:
            iccsale[itemname] = iccsale[itemname] + icc[itemname]*int(saleamt)
        if iccsale[itemname] > maxsale:
            maxsale = iccsale[itemname]
            topsale = [itemname]
        elif iccsale[itemname] == maxsale:
            topsale.append(itemname)
topsale.sort()
if iccsale == {}:
    print("No ice cream sales")
else:
    print("Total ice cream sales: " + str(float(sum([iccsale[k] for k in iccsale]))))
    print("Top sales: "+ ", ".join(topsale))