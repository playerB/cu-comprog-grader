def is_odd(n) :
    if n % 2 == 1 :
        return True
    else:
        return False

def has_odds(x) :
    for i in x :
        if is_odd(i) :
            return True
    return False

def all_odds(x) :
    for i in x :
        if not is_odd(i) :
            return False
    return True

def no_odds(x):
    return not has_odds(x)

def get_odds(x):
    odd = list()
    for i in x:
        if is_odd(i):
            odd.append(i)
    return odd

def zip_odds(a, b):
    zipodd = list(); i, j = 0, 0
    for r in range(len(get_odds(a)) + len(get_odds(b))):
        if (not is_odd(r) and i < len(get_odds(a))) or j == len(get_odds(b)):
            zipodd.append(get_odds(a)[i])
            i += 1
        else:
            if j < len(get_odds(b)) or i == len(get_odds(a)):
                zipodd.append(get_odds(b)[j])
                j += 1
    return zipodd
exec(input().strip())