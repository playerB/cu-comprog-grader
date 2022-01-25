snooker = ['X', 'R', 'Y', 'G', 'W', 'B', 'P', 'K']
p1 = 0; p2 = 0
while True:
    play  = input().strip()
    if len(play) == 3:
        if play[0] == '1':
            p1 += snooker.index(play[1]) + snooker.index(play[2])
        else:
            p2 += snooker.index(play[1]) + snooker.index(play[2])
    else:
        if play[0] == '1':
            p1 += snooker.index(play[1])
        else:
            p2 += snooker.index(play[1])
    if play[1] == 'K' and len(play) == 2: break
print(p1, p2)
if p1 > p2:
    print("Player 1 wins")
elif p2 > p1:
    print("Player 2 wins")
else:
    print("Tie")