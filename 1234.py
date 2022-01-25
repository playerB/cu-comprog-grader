class piggybank:
    def __init__(self):
        self.coins = dict()

    def add(self, v, n):
        v = float(v)
        n = int(n)
        if sum(self.coins.values()) + n <= 100:
            if v not in self.coins:
                self.coins[v] = 0
            self.coins[v] += n
            return True
        else:
            return False

    def __float__(self):
        val = 0.0
        for i in self.coins.keys():
            val += i*self.coins[i]
        return val

    def __str__(self):
        ret = list()
        for i in sorted(self.coins.keys()):
            ret.append(str(i) + ':' + str(self.coins[i]))
        st = '{' + ', '.join(ret) + '}'
        return st


cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)