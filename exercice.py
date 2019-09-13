# coding: utf-8

import operations_elementaires as oe
import operations_avancees as oa
import autres as a
import affichage as affich
from math import factorial
from fractions import Fraction as F
from itertools import product

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def tcheb(n):
    T_0 = [1]
    T_1 = [0,1]
    for _i in range(n-1): 
        T_1, T_0 = oe.diff(oe.produit([0,2], T_1), T_0), T_1
    return T_1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def pascal(n):
    row = list()
    k = 0
    for _i in range(n+1):
        row.append(binomial(n, k))
        k+=1
    return row

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def binomial(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def divisors(n):
    i=F(1)
    res = list()
    while i <= n:
        if n%i == 0:
            res.append(i)
        i+=F(1)
    return res

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def roots(P):
    c,b,a = P[0], P[1], P[2]
    return sorted(list(set([(-b + x*F((b*b - F(4)*a*c)**F(0.5))) / (F(2) * a) for x in [F(1), F(-1)]])))[::-1]
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def multiplicite(P, r):
    m = int()
    res = a.evalue(P, r)
    while P and res == 0:
        m += 1
        P = oa.derive(P)
        res = a.evalue(P,r)
    return m

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def factorized(P, m):
    poly = str()
    tool = {(False): "-", (True): "+"}
    a_n = P[-1]

    if a_n < 0:
        poly += "-{}".format(abs(a_n))
    else:
        poly += "{}".format(a_n)

    for root, mult in m:
        if root !=0:
            shape = {1: '(X{}{})'}.get(mult, '(X{}{})**({})')
            sign = tool[root<0]
            root = abs(root)
            poly += shape.format(sign, root, mult)
        if root ==0:
            shape = {1: 'X'}.get(mult, 'X**({})')
            poly += shape.format(mult)
    print(poly)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    print "On a :\nT_5 =",
    affich.affich(tcheb(5))
    print "\nEt on a :\nT_10 =",
    affich.affich(tcheb(10))
    print "\nLes coefficients binomiaux sont : " + " ".join("{}".format(n) for n in pascal(15))
    P = [F(2),F(-7),F(-6),F(34),F(10),F(-63),F(-22),F(44),F(24)]
    P_der = oa.derive(P)
    print "\nP' =",
    affich.affich(P_der)
    pgcd = oa.pgcd(P, P_der)
    print "\nP^P' =",
    affich.affich(pgcd)
    Q = oa.division(P, pgcd)[0]
    print "\nQ =",
    affich.affich(Q)
    if a.evalue(Q,F(-1)) == 0:
        print "\nVerification : -1 est une racine de Q"
    else:
        print "\nVerification : -1 n'est pas une racine de Q"
    Q_div = oa.division(Q,[1,1])[0] # (X+1) divise Q car -1 racine de Q
    racines = roots(Q_div) # Ce sont les racines du polynôme de degré 2
    racines.append(F(-1)) # On ajoute la racine connu de Q : -1
    print "\nLes racines de Q sont : " + ", ".join("{}".format(n) for n in racines)
    print "\nLes racines de P sont alors : " + ", ".join("{}".format(n) for n in racines)
    print "De plus : "
    root_mult = [(i, multiplicite(P, i)) for i in racines]

    for x,y in root_mult:
        print "La multiplicite de {} est {}".format(x,y)
    print"\nL'expression de P sous forme factorisee est alors : P =",
    factorized(P, root_mult)

    root = [i[0] for i in root_mult for _n in range(i[1])]
    P_verif = oe.produit([P[-1]], a.racine(root))
    print "\nLa forme developpe de l'expression precedente est :",
    affich.affich(P_verif)
    if P_verif == P:
        print "On retrouve bien la meme expression."
    else:
        print "Les expressions sont différentes."
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    main()
