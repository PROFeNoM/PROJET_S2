# coding: utf-8
# CHOURA Alexandre
# MATAVAR Axel

from fractions import Fraction as F

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def deg(P):
    while P and P[-1] == 0: # Cas d'un liste trompeuse, avec des zéros à la fin, sinon la boucle n'est pas éxécuté
        P.pop() 
    return len(P)-1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def unitaire(P): # La fonction ne retourne rien (None), c'est du in-place
    # Cas d'un liste trompeuse, avec des zéros à la fin, sinon la boucle n'est pas éxécuté
    while P[-1] == 0:
        P.pop()
        # Vérifie si la liste n'est pas alors vide, sinon renvoie le polynome nul
        if not P: 
            P.append(F(0))
            return
    coeff = P[-1]
    for i in range(len(P)):
        P[i] = F(P[i], coeff)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def monome(n): 
    return [F(0) for _i in range(n)] + [F(1)]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    print "Test de deg() :"

    # Test avec [F(2)]
    res = deg([F(2)])
    if res == 0:
        test = "OK"
    else:
        test = "NOK"
    print "\ndeg({}) = {} ; Resultat attendu = {}".format([F(2)], res, 0)
    print " ---> test {}".format(test)
    
    # Test avec [F(),F(),F(2)]
    res = deg([F(),F(),F(2)])
    if res == 2:
        test = "OK"
    else:
        test = "NOK"
    print "\ndeg({}) = {} ; Resultat attendu = {}".format([F(),F(),F(2)], res, 2)
    print " ---> test {}".format(test)

    # Test avec [F()]
    res = deg([F()])
    if res == -1:
        test = "OK"
    else:
        test = "NOK"
    print "\ndeg({}) = {} ; Resultat attendu = {}".format([F()], res, -1)
    print " ---> test {}".format(test)

     # Test avec [F(1),F(),F(8),F(-6),F()]
    res = deg([F(1),F(),F(8),F(-6),F()])
    if res == 3:
        test = "OK"
    else:
        test = "NOK"
    print "\ndeg({}) = {} ; Resultat attendu = {}".format([F(1),F(),F(8),F(-6),F()], res, 3)
    print " ---> test {}".format(test)

    # Test avec [F(1), F(-2), F(), F(3)]
    res = deg([F(1), F(-2), F(), F(3)])
    if res == 3:
        test = "OK"
    else:
        test = "NOK"
    print "\ndeg({}) = {} ; Resultat attendu = {}".format([F(1), F(-2), F(), F(3)], res, 3)
    print " ---> test {}".format(test)

    # Test avec [F(), F(), F(), F()] 
    res = deg([F(), F(), F(), F()] )
    if res == -1:
        test = "OK"
    else:
        test = "NOK"
    print "\ndeg({}) = {} ; Resultat attendu = {}".format([F(), F(), F(), F()], res, -1)
    print " ---> test {}".format(test)

    # Test avec [F(), F(1), F(1), F()] 
    res = deg([F(), F(1), F(1), F()])
    if res == 2:
        test = "OK"
    else:
        test = "NOK"
    print "\ndeg({}) = {} ; Resultat attendu = {}".format([F(), F(1), F(1), F()], res, 2)
    print " ---> test {}".format(test)

    print "\n\nTest de unitaire() :"

    # Test avec [F(1), F(-2), F(), F(3)]
    res = [F(1), F(-2), F(), F(3)]
    unitaire(res)
    if res == [F(1,3), F(-2,3), F(), F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nunitaire({}) = {} ; Resultat attendu = {}".format([F(1), F(-2), F(), F(3)], res, [F(1,3), F(-2,3), F(), F(1)])
    print " ---> test {}".format(test)

    # Test avec [F(), F(), F(), F()]
    res = [F(), F(), F(), F()]
    unitaire(res)
    if res == [F()]:
        test = "OK"
    else:
        test = "NOK"
    print "\nunitaire({}) = {} ; Resultat attendu = {}".format([F(), F(), F(), F()], res, [F()])
    print " ---> test {}".format(test)

    # Test avec [F(1), F(-2), F(), F(1)]
    res = [F(1), F(-2), F(), F(1)]
    unitaire(res)
    if res == [F(1), F(-2), F(), F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nunitaire({}) = {} ; Resultat attendu = {}".format([F(1), F(-2), F(), F(1)], res, [F(1), F(-2), F(), F(1)])
    print " ---> test {}".format(test)

    # Test avec [F(1), F(-2), F(), F(1,2)]
    res = [F(1), F(-2), F(), F(1,2)]
    unitaire(res)
    if res == [F(2), F(-4), F(), F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nunitaire({}) = {} ; Resultat attendu = {}".format([F(1), F(-2), F(), F(1,2)], res, [F(2), F(-4), F(), F(1)])
    print " ---> test {}".format(test)
    
    # Test avec [F(),F(3),F(6),F(2,3),F(7,6)]
    res = [F(),F(3),F(6),F(2,3),F(7,6)]
    unitaire(res)
    if res == [F(),F(18,7),F(36,7),F(4,7),F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nunitaire({}) = {} ; Resultat attendu = {}".format([F(),F(3),F(6),F(2,3),F(7,6)], res, [F(),F(18,7),F(36,7),F(4,7),F(1)])
    print " ---> test {}".format(test)


    print "\n\nTest de monome() :"
    
    # Test avec n=0
    res = monome(0)
    if res == [F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nmonome({}) = {} ; Resultat attendu = {}".format(0, res, [F(1)])
    print " ---> test {}".format(test)

    # Test avec n=2
    res = monome(2)
    if res == [F(), F(), F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nmonome({}) = {} ; Resultat attendu = {}".format(2, res, [F(), F(), F(1)])
    print " ---> test {}".format(test)

    # Test avec n=5
    res = monome(5)
    if res == [F(), F(), F(), F(), F(), F(1)]:
        test = "OK"
    else:
        test = "NOK"
    print "\nmonome({}) = {} ; Resultat attendu = {}".format(5, res, [F(), F(), F(), F(), F(), F(1)])
    print " ---> test {}".format(test)
        
