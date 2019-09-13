# coding: utf-8
# CHOURA Alexandre
# MATAVAR Axel

import bases as b
import operations_elementaires as oe
from fractions import Fraction as F
from itertools import izip
from affichage import affich

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def puissance(L, n):
    if n == 0:
        return [F(1)]
    res = L
    for _i in range(n-1):
        res = oe.produit(res, L)
    return res

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def division(L1,L2):
    deg_L2, deg_L1 = b.deg(L2), b.deg(L1)
    if deg_L2 < 0: # Polynome nul
        raise ZeroDivisionError
    if deg_L1 >= deg_L2:
        if deg_L1 == 0:
            return [0], L1
        if deg_L1 == 1:
            q = [0, 0]
        if deg_L2 == 0:
            return [i/L2[0] for i in L1], [F()]
        else:
            q = [0] * deg_L1 # Degré max du polynome final
        while deg_L1 >= deg_L2:
            d = [0]*(deg_L1 - deg_L2) + L2 # Amene le dénominateur au bon degré
            mult = q[deg_L1 - deg_L2] = L1[-1] / F(d[-1]) # Détermine le coefficient multipliacateur, et l'assigne à la liste final
            d = [coeff*mult for coeff in d] # Multiplie ce par quoi on va soustraire par le coeff
            L1 = [( coeff_L1 - coeff_d ) for coeff_L1, coeff_d in izip(L1, d)] # On effectue la soustraction
            deg_L1 = b.deg(L1) # Le degré du nouveau polyonome
        r = L1
    else:
        if L1 == []: L1 = [F()]
        return [F(0)], L1
    while q[-1] == 0:
        q.pop()
    if not r: r = [F()]
    return q, r

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def estdivisible(L1,L2):
    if division(L1, L2)[1] == [F()]: # Vérifie s'il y a un reste
        return True
    return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def pgcd(L1,L2):
    if L2 == [F()]:
        b.unitaire(L1)
        return L1
    R = division(L1,L2)[1]
    if R == [F()]:
        b.unitaire(L2)
        return L2
    while R:
        L1, L2 = L2, R
        last = R
        R = division(L1,L2)[1]
        if b.deg(R) < 1:
            if R == []:
                b.unitaire(last)
                return last
            else:
                last = R
                b.unitaire(last)
                return last
    # On rend le polynôme obtenu unitaire
    last = R
    b.unitaire(last)
    return last

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def derive(P):
    if len(P) <= 1:
        return [F(0)]
    else:
        return [coeff*power for power, coeff in enumerate(P) if power !=0]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
if __name__ == "__main__":
    print "Test de puissance() :"
    
    # Test avec [F(), F(5), F(), F(), F(-2)] et n=4
    res = puissance([F(), F(5), F(), F(), F(-2)], 4)
    if res == [F(), F(), F(), F(), F(625), F(), F(), F(-1000), F(), F(), F(600), F(), F(), F(-160), F(), F(), F(16)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npuissance{} = {} ; Resultat attendu = {}".format(([F(), F(5), F(), F(), F(-2)], 4), res, [F(), F(), F(), F(), F(625), F(), F(), F(-1000), F(), F(), F(600), F(), F(), F(-160), F(), F(), F(16)])
    print " ---> test {}".format(test)

    # Test avec [F(), F(5), F(), F(), F(-2)] et n=0
    res = puissance([F(), F(5), F(), F(), F(-2)], 0)
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npuissance{} = {} ; Resultat attendu = {}".format(([F(), F(5), F(), F(), F(-2)], 4), res, [F(1)])
    print " ---> test {}".format(test)

    print "\n\nTest de division() :"

    # Test avec [F()] et [F(1), F(2), F(1)]
    q, r = division([F()], [F(1), F(2), F(1)])
    if q == [F()] and r == [F()]:
        test = "OK"
    else:
        test = "NOK"
    print "\ndivision{} = quotient :{} \nreste : {} \nResultat attendu = quotient :{} \nreste : {}".format(([F()], [F(1), F(2), F(1)]), q, r, [F()], [F()])
    print " ---> test {}".format(test)
    
    # Test avec [F(3), F(), F(1)] et [F(1), F(2), F(1)]
    q, r = division([F(3), F(), F(1)], [F(1), F(2), F(1)])
    if q == [F(1)] and r == [F(2), F(-2)]:
        test = "OK"
    else:
        test = "NOK"
    print "\ndivision{} = quotient :{} \nreste : {} \nResultat attendu = quotient :{} \nreste : {}".format(([F(3), F(), F(1)], [F(1), F(2), F(1)]), q, r, [F(1)], [F(2), F(-2)])
    print " ---> test {}".format(test)

    # Test avec [F(3), F(), F(1)] et [F()]
    try:
        q, r = division([F(3), F(), F(1)], [F()])
    except ZeroDivisionError:
        print "\ndivision{} = {} \nResultat attendu = {}".format(([F(3), F(), F(1)], [F()]), ZeroDivisionError, ZeroDivisionError)
        test = "OK"
    else:
        test = "NOK"
    print " ---> test {}".format(test)

    # Test avec [F(3), F(), F(1)] et [F(1)]
    q, r = division([F(3), F(), F(1)], [F(1)])
    if q == [F(3), F(), F(1)] and r == [F()]:
        test = "OK"
    else:
        test = "NOK"
    print "\ndivision{} = quotient :{} \nreste : {} \nResultat attendu = quotient :{} \nreste : {}".format(([F(3), F(), F(1)], [F(1)]), q, r, [F(3), F(), F(1)], [F()])
    print " ---> test {}".format(test)
    
    # Test avec [F(3), F(), F(1)] et [F(1), F(2)]
    q, r = division([F(3), F(), F(1)], [F(1), F(2)])
    if q == [F(-1, 4), F(1, 2)] and r == [F(13, 4)]:
        test = "OK"
    else:
        test = "NOK"
    print "\ndivision{} = quotient :{} \nreste : {} \nResultat attendu = quotient :{} \nreste : {}".format(([F(3), F(), F(1)], [F(1), F(2)]), q, r, [F(-1, 4), F(1, 2)], [F(13, 4)])
    print " ---> test {}".format(test)

    # Test avec [F(3), F(2), F(1), F(), F(5), F(6), F(), F(1)] et [F(1), F(2)]
    q, r = division([F(3), F(2), F(1), F(), F(5), F(6), F(), F(1)], [F(1), F(2)])
    if q == [F(81, 128), F(47, 64), F(-15, 32), F(15, 16), F(25, 8), F(-1, 4), F(1, 2)] and r == [F(303, 128)]:
        test = "OK"
    else:
        test = "NOK"
    print "\ndivision{} = quotient :{} \nreste : {} \nResultat attendu = quotient :{} \nreste : {}".format(([F(3), F(2), F(1), F(), F(5), F(6), F(), F(1)], [F(1), F(2)]), q, r, [F(81, 128), F(47, 64), F(-15, 32), F(15, 16), F(25, 8), F(-1, 4), F(1, 2)], [F(303, 128)])
    print " ---> test {}".format(test)

    print "\n\nTest de la fonction estdivisible() :"

    # Test avec [F(3), F(2), F(1), F(), F(5), F(6), F(), F(1)] et [F(3), F(2), F(1), F(), F(5), F(6), F(), F(1)]
    res = estdivisible([F(3), F(2), F(1), F(), F(5), F(6), F(), F(1)],[F(3), F(2), F(1), F(), F(5), F(6), F(), F(1)])
    if res == True:
        test = "OK"
    else:
        test = "NOK"
    print "\nestdivisible{} = {} ;  Resultat attendu = {}".format(([F(3), F(2), F(1), F(), F(5), F(6), F(), F(1)],[F(3), F(2), F(1), F(), F(5), F(6), F(), F(1)]), res, True)
    print " ---> test {}".format(test)

    # Test avec [F(4),F(2)] et [F(2),F(1)]
    res = estdivisible([F(4),F(2)],[F(2),F(1)])
    if res == True:
        test = "OK"
    else:
        test = "NOK"
    print "\nestdivisible{} = {} ;  Resultat attendu = {}".format(([F(4),F(2)],[F(2),F(1)]), res, True)
    print " ---> test {}".format(test)

    # Test avec [F(2), F(1)] et [F(4),F(2), F(1)]
    res = estdivisible([F(2), F(1)],[F(4),F(2), F(1)])
    if res == False:
        test = "OK"
    else:
        test = "NOK"
    print "\nestdivisible{} = {} ;  Resultat attendu = {}".format(([F(2), F(1)],[F(4),F(2), F(1)]), res, False)
    print " ---> test {}".format(test)

    # Test avec [F(1), F(3)] et [F(2), F(4)]
    res = estdivisible([F(1), F(3)],[F(2), F(4)])
    if res == False:
        test = "OK"
    else:
        test = "NOK"
    print "\nestdivisible{} = {} ;  Resultat attendu = {}".format(([F(1), F(3)],[F(2), F(4)]), res, False)
    print " ---> test {}".format(test)

     # Test avec [F(1)] et [F(2), F(4)]
    res = estdivisible([F(1)],[F(2), F(4)])
    if res == False:
        test = "OK"
    else:
        test = "NOK"
    print "\nestdivisible{} = {} ;  Resultat attendu = {}".format(([F(1)],[F(2), F(4)]), res, False)
    print " ---> test {}".format(test)

    # Test avec [F(1), F(3)] et [F(2)]
    res = estdivisible([F(1), F(3)],[F(2)])
    if res == True:
        test = "OK"
    else:
        test = "NOK"
    print "\nestdivisible{} = {} ;  Resultat attendu = {}".format(([F(1), F(3)],[F(2)]), res, True)
    print " ---> test {}".format(test)

    print "\n\nTest de la fonction pgcd() :"

    # Test avec [F(2), F(-7), F(-6), F(34), F(10), F(63), F(-22), F(44), F(24)] et [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)]
    res = pgcd([F(2), F(-7), F(-6), F(34), F(10), F(63), F(-22), F(44), F(24)], [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)])
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(2), F(-7), F(-6), F(34), F(10), F(63), F(-22), F(44), F(24)], [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)]), res, [F(1)]) 
    print " --->test = {}".format(test)
    
    # Test avec [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)] et [F(2), F(-7), F(-6), F(34), F(10), F(63), F(-22), F(44), F(24)]
    res = pgcd([F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)], [F(2), F(-7), F(-6), F(34), F(10), F(63), F(-22), F(44), F(24)])
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)], [F(2), F(-7), F(-6), F(34), F(10), F(63), F(-22), F(44), F(24)]), res, [F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)] et [F(2), F(-7), F(-6), F(34), F(10), F(-63), F(-22), F(44), F(24)]
    res = pgcd([F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)], [F(2), F(-7), F(-6), F(34), F(10), F(-63), F(-22), F(44), F(24)])
    if res == [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)], [F(2), F(-7), F(-6), F(34), F(10), F(-63), F(-22), F(44), F(24)]), res, [F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F(2), F(-7), F(-6), F(34), F(10), F(-63), F(-22), F(44), F(24)] et [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)]
    res = pgcd([F(2), F(-7), F(-6), F(34), F(10), F(-63), F(-22), F(44), F(24)], [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)])
    if res == [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(2), F(-7), F(-6), F(34), F(10), F(-63), F(-22), F(44), F(24)], [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)]), res, [F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F(-7), F(-12), F(102), F(40), F(-315), F(-132), F(308), F(192)] et [F(2), F(), F(2), F(), F(1)]
    res = pgcd([F(-7), F(-12), F(102), F(40), F(-315), F(-132), F(308), F(192)], [F(2), F(), F(2), F(), F(1)])
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(-7), F(-12), F(102), F(40), F(-315), F(-132), F(308), F(192)], [F(2), F(), F(2), F(), F(1)]), res, [F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F(2), F(), F(2), F(), F(1)] et [F(-7), F(-12), F(102), F(40), F(-315), F(-132), F(308), F(192)]
    res = pgcd([F(2), F(), F(2), F(), F(1)], [F(-7), F(-12), F(102), F(40), F(-315), F(-132), F(308), F(192)])
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(2), F(), F(2), F(), F(1)], [F(-7), F(-12), F(102), F(40), F(-315), F(-132), F(308), F(192)]), res, [F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F(2), F(), F(2), F(), F(1)] et [F(1), F(1)]
    res = pgcd([F(2), F(), F(2), F(), F(1)], [F(1), F(1)])
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(2), F(), F(2), F(), F(1)], [F(1), F(1)]), res, [F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F(1), F(1)] et [F(2), F(), F(2), F(), F(1)]
    res = pgcd([F(1), F(1)], [F(2), F(), F(2), F(), F(1)])
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(1), F(1)], [F(2), F(), F(2), F(), F(1)]), res, [F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)] et [F(2), F(), F(2), F(), F(1)]
    res = pgcd([F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)], [F(2), F(), F(2), F(), F(1)])
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)], [F(2), F(), F(2), F(), F(1)]), res, [F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F(2), F(), F(2), F(), F(1)] et [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)]
    res = pgcd([F(2), F(), F(2), F(), F(1)], [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)])
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(2), F(), F(2), F(), F(1)], [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)]), res, [F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F(2), F(), F(2), F(), F(1)] et [F(1), F(), F(1)]
    res = pgcd([F(2), F(), F(2), F(), F(1)], [F(1), F(), F(1)])
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(2), F(), F(2), F(), F(1)], [F(1), F(), F(1)]), res, [F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F(1), F(), F(1)] et [F(2), F(), F(2), F(), F(1)]
    res = pgcd([F(1), F(), F(1)], [F(2), F(), F(2), F(), F(1)])
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(1), F(), F(1)], [F(2), F(), F(2), F(), F(1)]), res, [F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F(1), F(), F(1)] et [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)]
    res = pgcd([F(1), F(), F(1)], [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)])
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(1), F(), F(1)], [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)]), res, [F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)] et [F(1), F(), F(1)]
    res = pgcd([F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)], [F(1), F(), F(1)])
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(1,4), F(-1,4), F(-5,4), F(1,4), F(2), F(1)], [F(1), F(), F(1)]), res, [F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F()] et [F(1), F(), F(1)]
    res = pgcd([F()], [F(1), F(), F(1)])
    if res == [F(1), F(), F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F()], [F(1), F(), F(1)]), res, [F(1), F(), F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F()] et [F(1), F(), F(1)]
    res = pgcd([F(1), F(), F(1)], [F()])
    if res == [F(1), F(), F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(1), F(), F(1)], [F()]), res, [F(1), F(), F(1)]) 
    print " --->test = {}".format(test)

    # Test avec [F()] et [F(1), F(), F(2)]
    res = pgcd([F(1), F(), F(2)], [F()])
    if res == [F(1,2), F(), F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\npgcd{} = {} ; Resultat attendu = {}".format(([F(1), F(), F(2)], [F()]), res, [F(1,2), F(), F(1)]) 
    print " --->test = {}".format(test)
    
    print "\n\nTest de la fonction derive() :"

    # Test avec [F(), F(2), F(), F(1)]
    res = derive([F(), F(2), F(), F(1)])
    if res == [F(2), F(), F(3)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nderive({}) = {} ; Resultat attendu = {}".format([F(), F(2), F(), F(1)], res, [F(2), F(), F(3)])
    print " ---> test {}".format(test)

    # Test avec [F(2), F(1)]
    res = derive([F(2), F(1)])
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nderive({}) = {} ; Resultat attendu = {}".format([F(2), F(1)], res, [F(1)])
    print " ---> test {}".format(test)

    # Test avec [F(2)]
    res = derive([F(2)])
    if res == [F()]:
        test = "OK"
    else:
        test = "NOK"
    print "\nderive({}) = {} ; Resultat attendu = {}".format([F(2)], res, [F()])
    print " ---> test {}".format(test)

    # Test avec [F()]
    res = derive([F()])
    if res == [F()]:
        test = "OK"
    else:
        test = "NOK"
    print "\nderive({}) = {} ; Resultat attendu = {}".format([F()], res, [F()])
    print " ---> test {}".format(test)

    # Test avec [F(-1), F(), F(), F(6,8), F(), F(), F(-14,7), F(18,3)]
    res = derive([F(-1), F(), F(), F(6,8), F(), F(), F(-14,7), F(18,3)])
    if res == [F(), F(), F(9,4), F(), F(), F(-12), F(42)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nderive({}) = {} ; Resultat attendu = {}".format([F(-1), F(), F(), F(6,8), F(), F(), F(-14,7), F(18,3)], res, [F(), F(), F(9,4), F(), F(), F(-12), F(42)])
    print " ---> test {}".format(test)
