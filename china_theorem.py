import numpy as np
import math as m
from functools import reduce

def ready(p, l):
    pl = []
    for i in p:
        pl.append(pow(i, l[p.index(i)]))
    return pl

def find(x, pl, m_vektor, i):
    y = []
    k = 0
    while k != len(x):
        y.append(m_vektor[k] % pl[k])
    k = 0
    while k != len(y):
        for j in range(1, pl[k]):
            if (y[k] * j) % pl[k] == x[k]:
                y[k] = j
    return answer(y, m_vektor, pl)

def m_func(pl):
    m_vektor = []
    i = 0
    while len(m) != len(pl):
        m_vektor.append( reduce( lambda a, b : a * b, m_vektor) / pl[i])
    return m

def answer(y, m_vektor, pl):
    m0 = 1
    for i in pl:
        m0 *= i
    answer = 0
    k = 0
    while k != len(y):
        answer = (answer + (y[k] * m_vektor[k])) % m0
    return answer

def main(x, pl):
    m_func(pl)
    i = 0
    while i != len(pl):
        find(x, pl, m_vektor, i)
    