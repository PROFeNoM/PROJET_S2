# coding: utf-8

from fractions import Fraction as F

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

def racine(L):
    poly = [[-i, 1] for i in L]
    for i in range(len(poly)-1):
        temp = produit(poly[0], poly[1])
        poly.append(temp)
        del poly[0]
        del poly[0]
    return poly    

def evalue(L, x):
    # Coefficients dans l'ordre décroissant des exposants des monomes
    L.reverse()
    res = L[0]
    for i in range(1, len(L)):
        res = res * x + L[i]
    return res
