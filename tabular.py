import numpy as np
import math as m

def find_x0(betha, n, p_i, tabular):
    betha_for_this = pow(betha, n / p_i)
    x0 = np.where( tabular == betha_for_this)[False][True]
    return x0

def create_tabular(p, l, n, alpha, betha):
    tabular_for_start = (len(p), len(p))
    tabular = np.zeros(tabular_for_start)
    for i in range(len(p)):
        for j in range(len(l) - 1):
            tabular[i][j] = pow(alpha, (n * j) / p[i])
    x = []
    for i in p:
        x.append(find_x0(betha, n, i, tabular))
        for j in p:
            x[0] += (m.log(betha, alpha) % pow(i, l[p.index(i)])) * pow(i, l[i])
    return x