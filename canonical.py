import math as m

def prime_check(a):
    for i in range(2, int(m.sqrt(a))):
        if a % i == 0:
            return bool(False)
    return bool(True)

def check_canonical(n, p, l):
    n_check = 1
    i = 0
    while i != len(p):
        n_check *= pow(p[i], l[i])
        i += 1
    if n_check == n:
        return bool(True)
    else:
        return bool(False)

def canonical(n):
    p = []
    l = []
    while n != 1:
        for i in range(2, int(m.sqrt(n))):
            if prime_check(i) == bool(True):
                if n % i == 0:
                    if i in p:
                        l[p.index(i)] += 1
                    else:
                        p.append(i)
                        l.append(1)
        n /= i
    if check_canonical(n, p, l) == bool(True):
        return p, l
    else:
        return 'канонічний розклад невірний'