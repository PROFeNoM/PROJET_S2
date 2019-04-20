# coding: utf-8

from fractions import Fraction as F

def deg(P):
    # Cas d'un liste vide
    if not P:
        return -1
    # Cas d'une liste trompeuse, avec des zéros à la fin, sinon la boucle n'est pas éxéxcuté 
    while P[-1] == 0:
        P.pop()
        # Vérifie si la liste n'est pas alors vide
        if not P: 
            return -1
    # Renvoit alors la valeur attendu
    return len(P) - 1


def unitaire(P):
    # Cas d'un liste trompeuse, avec des zéros à la fin, sinon la boucle n'est pas éxécuté
    while P[-1] == 0:
        P.pop()
        # Vérifie si la liste n'est pas alors vide, sinon renvoie le polynome nul
        if not P: 
            return [F(0)]
    coeff = P[-1]
    # Divise tous les coefficients par ce coefficient
    return [F(i, coeff) for i in P]

def monome(n):
    P = [F(0) for _i in range(n+1)]
    P[-1] = F(1)
    return P
