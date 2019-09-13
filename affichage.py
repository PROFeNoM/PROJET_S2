# coding: utf-8
# CHOURA Alexandre
# MATAVAR Axel

from fractions import Fraction as F


def affich(P):
    global poly
    poly = str()
    # le dictionnaire tool va nous permettre de déterminer le signe à afficher pour le coefficient
    tool = {(False, True): '-', (True, False): ' + ', (True, True): '', (False, False): ' - '}
    # enumerate() permet d'avoir la puissance à travers l'index de l'element dans P
    # On reverse la list pour l'ordre d'affichage
    for power, coeff in reversed(list(enumerate(P))):
        if coeff !=0:
            # shape agit en tant que dictionnaire nous permettant de prendre le forme à print souhaité
            shape = {0: '{}{}', 1: '{}{}X'}.get(power, '{}{}X**{}')
            # Si le premier coefficient est positif, on ne veut pas afficher de "+" devant, d'où le not poly
            sign = tool[coeff > 0, not poly]
            coeff = abs(coeff)
            # On ne veut pas afficher "1X**", sauf si la puissance est nulle
            if power != 0 and coeff == 1:
                coeff = ""
            # On concatène comme voulu
            poly += shape.format(sign, coeff, power)
    if not poly:
        poly = "0"
    print(poly)

if __name__ == "__main__":
    print "Test de affich() :"

    # Test avec [F(1), F(-2), F(), F(3)]  
    print "\naffich({}) =".format([F(1), F(-2), F(), F(3)]), 
    affich([F(1), F(-2), F(), F(3)])
    print "Resultat attendu = {}".format("3X**3 - 2X + 1")
    if poly == "3X**3 - 2X + 1":
        test = "OK"
    else:
        test = "NOK"
    print " ---> test {}".format(test)

    # Test avec [F(), F(1), F(), F()]  
    print "\naffich({}) =".format([F(), F(1), F(), F()]  ), 
    affich([F(), F(1), F(), F()])
    print "Resultat attendu = {}".format("X")
    if poly == "X":
        test = "OK"
    else:
        test = "NOK"
    print " ---> test {}".format(test)

    # Test avec [F(), F(1), F(1), F()]  
    print "\naffich({}) =".format([F(), F(1), F(1), F()]), 
    affich([F(), F(1), F(1), F()])
    print "Resultat attendu = {}".format("X**2 + x")
    if poly == "X**2 + X":
        test = "OK"
    else:
        test = "NOK"
    print " ---> test {}".format(test)

    # Test avec [F(), F(), F(), F()]  
    print "\naffich({}) =".format([F(), F(), F(), F()]), 
    affich([F(), F(), F(), F()])
    print "Resultat attendu = {}".format("0")
    if poly == "0":
        test = "OK"
    else:
        test = "NOK"
    print " ---> test {}".format(test)

    # Test avec [F(1),F(1),F(-3),F(0),F(2,3)]
    print "\naffich({}) =".format([F(1),F(1),F(-3),F(0),F(2,3)]), 
    affich([F(1),F(1),F(-3),F(0),F(2,3)])
    print "Resultat attendu = {}".format("2/3X**4 - 3X**2 + X + 1")
    if poly == "2/3X**4 - 3X**2 + X + 1":
        test = "OK"
    else:
        test = "NOK"
    print " ---> test {}".format(test)

    # Test avec [F(),F(-1),F(),F(4),F(),F()]
    print "\naffich({}) =".format([F(),F(-1),F(),F(4),F(),F()]), 
    affich([F(),F(-1),F(),F(4),F(),F()])
    print "Resultat attendu = {}".format("4X**3 - X")
    if poly == "4X**3 - X":
        test = "OK"
    else:
        test = "NOK"
    print " ---> test {}".format(test)

    # Test avec [F(-1),F(-1)]
    print "\naffich({}) =".format([F(-1),F(-1)]), 
    affich([F(-1),F(-1)])
    print "Resultat attendu = {}".format("-X - 1")
    if poly == "-X - 1":
        test = "OK"
    else:
        test = "NOK"
    print " ---> test {}".format(test)
