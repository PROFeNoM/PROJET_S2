# coding: utf-8

from fractions import Fraction as F
import operations_elementaires as oe

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def racine(L):
    if len(L) == 0:
        return [F(0)]
    # On va développer
    poly = [[-i, 1] for i in L]
    for i in range(len(poly)-1):
        temp = oe.produit(poly[0], poly[1])
        poly.append(temp)
        del poly[0]
        del poly[0]
    return poly[0]  

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def evalue(P,x):		#Application de l'algorithme d'Horner
	a=P[len(P)-1]
	for i in range(len(P)-2,-1,-1):
		a=x*a+P[i]
	return a

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
if __name__ == "__main__":
    print "Test de racine() :"
    # Test avec [F(),F()] : 0 racine double
    res = racine([F(),F()])
    if res == [F(), F(), F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "racine({}) = {} ; Resultat attendu = {}".format([F(),0], res, [F(), F(), F(1)])
    print " ---> test {}".format(test)

    # Test avec [F(16), F(-2), F(), F(3), F(3)] : 0 racine double
    res = racine([F(16), F(-2), F(), F(3), F(3)])
    if res == [F(), F(-288), F(66), F(61), F(-20), F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nracine({}) = {} ; Resultat attendu = {}".format([F(16), F(-2), F(), F(3), F(3)], res, [F(), F(-288), F(66), F(61), F(-20), F(1)])
    print " ---> test {}".format(test)

    # Test avec [F(1658992),F(1658992)] : 1658992 racine double
    res = racine([F(1658992),F(1658992)])
    if res == [F(1658992**2), F(-3317984), 1]:
        test = "OK"
    else:
        test = "NOK"
    print "\nracine({}) = {} ; Resultat attendu = {}".format([F(1658992),F(1658992)], res, [F(1658992**2), F(-3317984), 1])
    print " ---> test {}".format(test)

    print "\n\nTest de evalue() :"
    
    # Test avec [F(),F()] en 0:
    res = evalue([F(),F()],0)
    if res == 0:
        test = "OK"
    else:
        test = "NOK"
    print "\nevalue{} = {} ; Resultat attendu = {}".format(([F(),F()],0), res, 0)
    print " ---> test {}".format(test)

    # Test avec [F(1), F(3), F(4), F(2)] en F(5,2)
    res = evalue([F(1), F(3), F(4), F(2)], F(5,2))
    if res == F(259, 4):
        test = "OK"
    else:
        test = "NOK"
    print "\nevalue{} = {} ; Resultat attendu = {}".format(([F(1), F(3), F(4), F(2)], F(5,2)),res, F(259, 4))
    print " ---> test {}".format(test)

    # Test avec [F(2752254456064), F(-3317984), F(1)] en F(1658992) : 1658992 est racine double
    res = evalue([F(2752254456064), F(-3317984), F(1)], F(1658992))
    if res == F():
        test = "OK"
    else:
        test = "NOK"
    print "\nevalue{} = {} ; Resultat attendu = {}".format(([F(2752254456064), F(-3317984), F(1)], F(1658992)), res, 0)
    print " ---> test {}".format(test)

    # Test avec [F(-2), F(43), F(-2), F(100), F(-95, 7), F(-13, 7), F(15,4), F(18, 7)] en F(527, 4)
    res = evalue([F(-2), F(43), F(-2), F(100), F(-95, 7), F(-13, 7), F(15, 4), F(18, 7)], F(527, 4))
    if res == F(205451243411117314535, 114688):
        test = "OK"
    else:
        test = "NOK"
    print "\nevalue{} = {} ; Resultat attendu = {}".format(([F(-2), F(43), F(-2), F(100), F(-95, 7), F(-13, 7), F(15,4), F(18, 7)], F(527, 4)), res, F(205451243411117314535, 114688))
    print " ---> test {}".format(test)
