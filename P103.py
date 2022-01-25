m = int(input().strip())
n = 0; sc1 = 0; sc2 = 0; tie = False
while True:
    if n == 3*m :
        tie = True
        break
    rps1, rps2 = input().strip().split()
    if rps1 == 'R' and rps2 == 'P':
        sc2 += 1
    elif rps1 == 'P' and rps2 == 'R':
        sc1 += 1
    elif rps1 == 'P' and rps2 == 'S':
        sc2 += 1
    elif rps1 == 'S' and rps2 == 'P':
        sc1 += 1
    elif rps1 == 'R' and rps2 == 'S':
        sc1 += 1
    elif rps1 == 'S' and rps2 == 'R':
        sc2 += 1
    if sc1 == m or sc2 == m:
        break
    n += 1
print(sc1, sc2)
if tie == False :
    if sc1 > sc2:
        print("Player 1 wins")
    elif sc2 > sc1 :
        print("Player 2 wins")
else:
    print("Tie")