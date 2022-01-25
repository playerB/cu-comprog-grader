class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'

    def next1(self):
        cardvalue = ('3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2')
        cardsuit = ('club', 'diamond', 'heart', 'spade')
        if self.suit != 'spade':
            ret = Card(self.value, cardsuit[cardsuit.index(self.suit) + 1])
        elif self.value != '2' and self.suit == 'spade':
            ret = Card(cardvalue[cardvalue.index(self.value) + 1], 'club')
        else:
            ret = Card('3', 'club')
        return ret

    def next2(self):
        cardvalue = ('3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2')
        cardsuit = ('club', 'diamond', 'heart', 'spade')
        if self.suit != 'spade':
            self.suit = cardsuit[cardsuit.index(self.suit) + 1]
        elif self.value != '2' and self.suit == 'spade':
            self.value = cardvalue[cardvalue.index(self.value) + 1]
            self.suit = 'club'
        else:
            self.value = '3'
            self.suit = 'club'


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])