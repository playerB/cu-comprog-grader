class roman:
    def __init__(self, r):
        self.r = r
        romannum = {'M':1000, 'D':500, 'C':100, 'CD':400, 'CM':900, 'L':50, 'X':10, 'XL':40, 'XC':90, 'V':5, 'I':1, 'IV':4, 'IX':9}
        self.val = 0
        i = 0
        while i < len(self.r):
            if self.r[i] in romannum.keys():
                if i+1 < len(self.r) and self.r[i:i+2] in romannum.keys():
                    self.val += romannum[self.r[i:i+2]]
                    i += 1
                else:
                    self.val += romannum[self.r[i]]
            i += 1

    def __lt__(self, other):
        return self.val < other.val

    def __str__(self):
        romannum = {'M':1000, 'D':500, 'C':100, 'CD':400, 'CM':900, 'L':50, 'X':10, 'XL':40, 'XC':90, 'V':5, 'I':1, 'IV':4, 'IX':9}
        numroman = {v: k for k, v in romannum.items()} #Lazy af
        myroman = ''
        while self.val != 0:
            for i in sorted(numroman.keys(), reverse=True):
                while self.val - i >= 0:
                    self.val -= i
                    myroman += numroman[i]
        return myroman

    def __int__(self):
        return int(self.val)

    def __add__(self, other):
        self.val += other.val
        return self

t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))