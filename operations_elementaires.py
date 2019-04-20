# coding: utf-8

from fractions import Fraction as F
from itertools import izip_longest

def somme(P, Q):
    s, l = sorted([P, Q], key=lambda p: len(p))
    poly = [sum(f) for f in zip(s, l)]
    poly.extend(l[len(s):])
    return poly

def diff(P,Q):
    poly = [a - b for a, b in izip_longest(P,Q, fillvalue = 0)]
    poly.extend([-i for i in Q[len(P):]])
    return poly

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
