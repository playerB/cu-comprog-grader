def read_date():
    dmy = input().strip().split()
    dmy[0] = int(dmy[0]); dmy[2] = int(dmy[2])
    m = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    if dmy[1] in m :
        dmy[1] = m.index(dmy[1])
    return dmy

def zodiac(d, m):
    zod = ['Aquarius','Pisces','Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn']
    dayinzod = [[1,21],[2,21],[3,22],[4,22],[5,22],[6,22],[7,22],[8,22],[9,22],[10,22],[11,22],[12,22]]
    for i in range(len(dayinzod)):
        if dayinzod[i] <= [int(m),int(d)] < dayinzod[i+1]:
            z = zod[i]
            break
        else:
            z = zod[11]
    return z

def days_in_feb(y):
    if y%4 == 0 and (y%100 != 0 or y%400 == 0):
        return 29
    return 28

def days_in_month(m, y):
    if m == 2:
        return days_in_feb(y)
    elif m in [4,6,9,11]:
        return 30
    return 31

def days_in_between(d1,m1,y1,d2,m2,y2):
    dd = d2 + days_in_month(m1,y1) - d1 -1
    for y in range(y1, y2+1):
        if y == y1 :
            for m in range(m1+1,13):
                dd += days_in_month(m,y)
        elif y == y2:
            for m in range(1,m2):
                dd += days_in_month(m,y)
        else:
            for m in range(1,13):
                dd += days_in_month(m,y)
    return dd

def main():
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    print(zodiac(d1,m1), zodiac(d2,m2))
    print(days_in_between(d1,m1,y1,d2,m2,y2))

exec(input().strip())