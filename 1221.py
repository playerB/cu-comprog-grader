class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        tostr_a = ''; tostr_b = ''; isplus = ''; isimgi = ''
        if self.a != 0: tostr_a = str(self.a)
        if self.b != 0: tostr_b = str(self.b)
        if tostr_a == '' and tostr_b == '': tostr_a = '0'
        if len(tostr_a) > 0 and len(tostr_b) > 0 and self.b > 0: isplus = '+'
        if len(tostr_b) > 0: isimgi = 'i'
        if self.b == 1: tostr_b = ''
        if self.b == -1: tostr_b = '-'
        return tostr_a + isplus + tostr_b + isimgi

    def __add__(self, rhs):
        a = self.a + rhs.a
        b = self.b + rhs.b
        return Complex(a, b)

    def __mul__(self, rhs):
        a = self.a * rhs.a - self.b * rhs.b
        b = self.a * rhs.b + self.b * rhs.a
        return Complex(a, b)

    def __truediv__(self, rhs):
        a = (self.a * rhs.a + self.b * rhs.b) / (rhs.a**2 + rhs.b**2)
        b = (self.b * rhs.a - self.a * rhs.b) / (rhs.a**2 + rhs.b**2)
        return Complex(a, b)

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a, b)
c2 = Complex(c, d)
if t == 1: print(c1)
elif t == 2: print(c2)
elif t == 3: print(c1 + c2)
elif t == 4: print(c1 * c2)
else: print(c1 / c2)