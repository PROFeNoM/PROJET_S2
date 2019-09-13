# coding: utf-8

from fractions import Fraction as F
from itertools import izip_longest

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def somme(P,Q):
    return [a + b for a, b in izip_longest(P,Q, fillvalue = 0)]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def diff(P,Q):
    return [a - b for a, b in izip_longest(P,Q, fillvalue = 0)]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def produit(P, Q):
    if not P or not Q: return [F()]
    
    # Cas de listes trompeuses, avec des zéros à la fin, sinon la boucle n'est pas éxéxcuté 
    while P[-1] == 0:
        P.pop()
        if not P: 
            return [F()]
    while Q[-1] == 0:
        Q.pop()
        if not Q : 
            return [F()]

    # Créer une liste de la bonne longueur, que l'on utilise par la suite
    res = [0 for i in range(len(P)+len(Q)-1)]
    # on distribue et additionne, en faisant correspondre au bon degré (i+j)
    for i,a in enumerate(P):
        for j,b in enumerate(Q):
            res[i + j] += a*b
    return res

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    print "Test de somme() :"

    # Test avec [F(5), F(1), F(9), F(7)] et [F(12), F(4), F(2), F(1)]
    res = somme([F(5), F(1), F(9), F(7)], [F(12), F(4), F(2), F(1)])
    if res == [F(17), F(5), F(11), F(8)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nsomme{} = {} ; Resultat attendu = {}".format(([F(5), F(1), F(9), F(7)], [F(12), F(4), F(2), F(1)]), res, [F(17), F(5), F(11), F(8)])
    print " ---> test {}".format(test)

    # Test avec [F(12), F(-1), F(-12), F(), F(2)] et [F(1), F(3), F(-2), F(1)]
    res = somme([F(12), F(-1), F(-12), F(), F(2)], [F(1), F(3), F(-2), F(1)])
    if res == [F(13), F(2), F(-14), F(1), F(2)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nsomme{} = {} ; Resultat attendu = {}".format(([F(12), F(-1), F(-12), F(2)], [F(1), F(3), F(-2), F(1)]), res, [F(13), F(2), F(-14), F(1), F(2)])
    print " ---> test {}".format(test)

    # Test avec [F(12), F(-1), F(-12), F(), F(2)] et []
    res = somme([F(12), F(-1), F(-12), F(), F(2)], [])
    if res == [F(12), F(-1), F(-12), F(), F(2)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nsomme{} = {} ; Resultat attendu = {}".format(([F(12), F(-1), F(-12), F(), F(2)], []), res, [F(12), F(-1), F(-12), F(), F(2)])
    print " ---> test {}".format(test)

    print "\n\nTest de diff() :"

    # Test avec [F(5), F(1), F(9), F(7)] et [F(12), F(4), F(2), F(1)]
    res = diff([F(5), F(1), F(9), F(7)], [F(12), F(4), F(2), F(1)])
    if res == [F(-7), F(-3), F(7), F(6)]:
        test = "OK"
    else:
        test = "NOK"
    print "\ndiff{} = {} ; Resultat attendu = {}".format(([F(5), F(1), F(9), F(7)], [F(12), F(4), F(2), F(1)]), res, [F(-7), F(-3), F(7), F(6)])
    print " ---> test {}".format(test)

    # Test avec [F(12), F(-1), F(-12), F(), F(2)] et [F(1), F(3), F(-2), F(1)]
    res = diff([F(12), F(-1), F(-12), F(), F(2)], [F(1), F(3), F(-2), F(1)])
    if res == [F(11), F(-4), F(-10), F(-1), F(2)]:
        test = "OK"
    else:
        test = "NOK"
    print "\ndiff{} = {} ; Resultat attendu = {}".format(([F(12), F(-1), F(-12), F(2)], [F(1), F(3), F(-2), F(1)]), res, [F(11), F(-4), F(-10), F(-1), F(2)])
    print " ---> test {}".format(test)

    # Test avec [] et [F(12), F(-1), F(-12), F(), F(2)]
    res = diff([F()], [F(12), F(-1), F(-12), F(), F(2)])
    if res == [F(-12), F(1), F(12), F(), F(-2)]:
        test = "OK"
    else:
        test = "NOK"
    print "\ndiff{} = {} ; Resultat attendu = {}".format(([], [F(12), F(-1), F(-12), F(), F(2)]), res, [F(-12), F(1), F(12), F(), F(-2)])
    print " ---> test {}".format(test)

    print "Test de produit() :"

    # Test avec [F(-4),F(2)] et [F(-5), F(1)]
    res = produit([F(-4),F(2)], [F(-5), F(1)])
    if res == [F(20), F(-14), F(2)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nproduit{} = {} ; Resultat attendu = {}".format(([F(-4),F(2)], [F(-5), F(1)]), res, [F(20), F(-14), F(2)])
    print " ---> test {}".format(test)

    # Test avec [F()] et [F(-5), F(1)]
    res = produit([F()], [F(-5), F(1)])
    if res == [F()]:
        test = "OK"
    else:
        test = "NOK"
    print "\nproduit{} = {} ; Resultat attendu = {}".format(([F()], [F(-5), F(1)]), res, [F()])
    print " ---> test {}".format(test)

    # Test avec [F(-10), F(1), F(), F(5)] et [F(), F(), F(2), F(), F(), F(1)]
    res = produit([F(-10), F(1), F(), F(5)], [F(), F(), F(2), F(), F(), F(1)])
    if res == [F(), F(), F(-20), F(2), F(), F(), F(1), F(), F(5)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nproduit{} = {} ; Resultat attendu = {}".format(([F(-10), F(1), F(), F(5)], [F(), F(), F(2), F(), F(), F(1)]), res, [F(), F(), F(-20), F(2), F(), F(), F(1), F(), F(5)])
    print " ---> test {}".format(test)

    # Test avec [F(), F(5), F(), F(), F(-2)] et [F(), F(5), F(), F(), F(-2)]
    res = produit([F(), F(5), F(), F(), F(-2)], [F(), F(5), F(), F(), F(-2)])
    if res == [F(0, 1), F(0, 1), F(25, 1), F(0, 1), F(0, 1), F(-20, 1), F(0, 1), F(0, 1), F(4, 1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nproduit{} = {} ; Resultat attendu = {}".format(([F(), F(5), F(), F(), F(-2)], [F(), F(5), F(), F(), F(-2)]), res, [F(0, 1), F(0, 1), F(25, 1), F(0, 1), F(0, 1), F(-20, 1), F(0, 1), F(0, 1), F(4, 1)])
    print " ---> test {}".format(test)
