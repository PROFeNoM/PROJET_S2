# coding: utf-8

from fractions import Fraction as F
from itertools import izip
from math import fabs

def deg(P):
    while P and P[-1] == 0:
        P.pop() 
    return len(P)-1

def produit(P, Q):
    if not P or not Q: return []
    
    # Cas de listes trompeuses, avec des zéros à la fin, sinon la boucle n'est pas éxéxcuté 
    while P[-1] == 0:
        P.pop()
        if not P: 
            return []
    while Q[-1] == 0:
        Q.pop()
        if not Q : 
            return []

    # Créer une liste de la bonne longueur, que l'on utilise par la suite
    res = [0 for i in range(len(P)+len(Q)-1)]
    # on distribue et additionne, en faisant correspondre au bon degré (i+j)
    for i,a in enumerate(P):
        for j,b in enumerate(Q):
            res[i + j] += a*b
    return res

def puissance(L, n):
    res = L
    for _i in range(n-1):
        res = produit(res, L)
    return res

def division(L1,L2):
    deg_L2, deg_L1 = deg(L2), deg(L1)
    if deg_L2 < 0: # Polynome nul
        raise ZeroDivisionError
    if deg_L1 >= deg_L2:
        if deg_L1 == 0:
            return [0], L1
        if deg_L1 == 1 :
            q = [0, 0]
        else:
            q = [0] * deg_L1 # Degré du polynome final
        while deg_L1 >= deg_L2:
            d = [0]*(deg_L1 - deg_L2) + L2 # Amene le dénominateur au bon degré
            mult = q[deg_L1 - deg_L2] = L1[-1] / F(d[-1]) # Détermine le coefficient multipliacateur, et l'assigne à la liste final
            d = [coeff*mult for coeff in d] # Multiplie ce par quoi on va soustraire par le coeff
            L1 = [( coeff_L1 - coeff_d ) for coeff_L1, coeff_d in izip(L1, d)] # On effectue la soustraction
            deg_L1 = deg(L1) # Le degré du nouveau polyonome
        r = L1
    else:
        return [0], L1
    return q, r

def estdivisible(L1,L2):
    if not division(L1, L2)[1]:
        return "Vrai"
    return "Faux"

def pgcd(L1,L2):
    R = division(L1,L2)[1]
    if not R:
        return L2
    while R:
        L1, L2 = L2, R
        last = R
        R = division(L1,L2)[1]
        if deg(R) <= 1:
            return last
    return last

def derive(P):
    return [coeff*power for power, coeff in enumerate(P) if power !=0]
