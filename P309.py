allOta = dict(); membersVote = dict(); allOchi = dict(); allCami = dict()
while True:
    inp = input().strip().split()
    if len(inp) < 3: break
    else: ota = inp[0]; ochi = inp[1]; vote = int(inp[2])
    if ota not in allOta: allOta[ota] = {ochi: vote}
    elif ochi not in allOta[ota]: allOta[ota][ochi] = vote
    else: allOta[ota][ochi] += vote
    if ochi not in membersVote: membersVote[ochi] = vote
    else: membersVote[ochi] += vote
    if ochi not in allOchi: allOchi[ochi] = {ota}
    else: allOchi[ochi].add(ota)
#list comprehension challenge : one liner
if inp[0] == '1':
    print(', '.join([member for vote, member in sorted([[-v, k] for k, v in membersVote.items()])[:3]]))
    # sort membersVote dict by -1*value and pick 1st-3rd member and join with ,
elif inp[0] == '2':
    print(', '.join([member for otaN, member in sorted([[-len(v), k] for k, v in allOchi.items()])[:3]]))
    # sort allOchi dict by -1*amt of ota and pick 1st-3rd member and join with ,
elif inp[0] == '3':
    print(', '.join([i[1] for i in sorted([[-([membervote[0][1] for otaname, membervote in [[k, sorted([[-vote, member] for member, vote in v.items()])[:1]] for k, v in allOta.items()]].count(mem)), mem] for mem in allOchi])][:3]))
    # sort allOta dict by most voted member of each ota and count their occurrences, sorted it again and join with ,