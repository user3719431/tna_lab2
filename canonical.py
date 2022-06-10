import numpy as np
import math as m

def prime_check(a):
    for i in range(2, int(m.sqrt(a))):
        if a % i == 0:
            return bool(False)
    return bool(True)

def canonical(n):
    p = []
    l = []
    while n != 1:
        for i in range(2, int(m.sqrt(n))):
            if prime_check(i) == bool(True):
                if n % i == 0:
                    if p == i:
                        l.insert(p.index(i), l(a.index(i)) + 1)
                    else:
                        p.append(i)
                        l.append(1)
    