cards = input().strip()
value = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
suit = ['', 'C', 'D', 'H', 'S']
mycards = list(); result = ''
for i in range(len(cards) // 2):
    mycards.append(cards[i*2: i*2+2])
for i in range(len(mycards) -1):
    if value.index(mycards[i][0]) > value.index(mycards[i+1][0]):
        result += '+' + str(value.index(mycards[i][0]) - value.index(mycards[i+1][0]))
    elif value.index(mycards[i][0]) < value.index(mycards[i+1][0]):
        result += '-' + str(value.index(mycards[i+1][0]) - value.index(mycards[i][0]))
    elif suit.index(mycards[i][1]) > suit.index(mycards[i+1][1]):
        result += '+' + str(suit.index(mycards[i][1]) - suit.index(mycards[i+1][1]))
    elif suit.index(mycards[i][1]) < suit.index(mycards[i+1][1]):
        result += '-' + str(suit.index(mycards[i+1][1]) - suit.index(mycards[i][1]))
    else:
        result += '0'
print(result)