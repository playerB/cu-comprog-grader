subs = int(input())
suffix = ""
if subs <= 1000 :
    suffix = ""
elif 1000 <= subs <= 1000000 :
    if subs <= 10000 :
        subs = (subs + 50) // 100 / 10
    else :
        subs = (subs + 500) // 1000
    suffix = "K"
elif 1000000 <= subs <= 1000000000 :
    if subs <= 10000000 :
        subs = (subs + 50000) // 100000 / 10
    else :
        subs = (subs + 500000) // 1000000
    suffix = "M"
elif 1000000000 <= subs :
    if subs <= 10000000000 :
        subs = (subs + 50000000) // 100000000 / 10
    else :
        subs = (subs + 500000000) // 1000000000
    suffix = "B"
print(str(subs) + suffix)