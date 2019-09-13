# coding: utf-8

from fractions import Fraction as F
import bases
import autres
import operations_avancees as oa

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def recherche(P,a,b,eps = 1e-2): # Un peu long
    """ Recherche un intervalle satisfaisant les hypotheses pour appliquer la dichotomie
        On procede par pas de epsilon, et si le produit des images est négatif, alors on
        utilise cet intervalle pour la suite """
    low, high = a, a+eps
    P_a, P_aeps = autres.evalue(P, a), autres.evalue(P, high)
    while P_a*P_aeps > 0:
        if high > b: # L'intervalle n'est plus bon, sans racines, inutile de continuer
            return None,None
        high += eps
        P_aeps = autres.evalue(P, high) # On a calcul les images des bornes de l'intervalle
    return low,high

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dichotomie(P,low,high,eps=1e-9):
    P_1 = autres.evalue(P, low)
    if P_1 == 0: # Verifie si low est racine et retourne la valeur si c'est le cas
        return low
    P_2 = autres.evalue(P, high) # Verifie si high est racine et retourne la valeur si c'est le cas
    if P_2 == 0:
        return high
    # L'intervalle satisfait les conduit pour le TVI (et donc la dichotomie)
    while high - low > eps: # On effectue la dichotomie pour une precision eps
        milieu = F(1,2)*(low + high)
        P_m = autres.evalue(P, milieu)
        if P_m == 0: # Verifie si la valeur du milieu est racine et la retourne si c'est le cas
            return milieu
        if P_2*P_m <= 0:
            low, P_1 = milieu, P_m
        else:
            high, P_2 = milieu, P_m
    return (low + high)/2.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def bonus(P):
    root = list()
    for _i in range(bases.deg(P)):
        # On calcul la somme
        s = int()
        for i in P[:len(P)-1]:
            s += abs(i)
        # Alpha (a) prend la valeur max
        a = max(1, s)
        # On détermine béta (b)
        b = 1 + max([abs(i) for i in P[:len(P)-1]])
        # Le minimum (mn) est alors:
        mn = min(a,b)
        mn = min(a,b)
        # On a alors un encadrement dans lequel ce situent toutes les racines de P : -mn <= x <= mn
        # Le polynome a au plus n racines reelles
        low = -mn # Borne sup
        high = mn # Borne inf
        if autres.evalue(P,low)*autres.evalue(P,high) <= 0:
            r = dichotomie(P, low, high) # On realise la dichotomie avec l'intervalle
            res = round(r, 2) # On arrondit arbitrairement a une valeur approche de 3 chiffres apres la virgule
            P = oa.division(P,[F(-res), F(1)])[0]
            bases.unitaire(P)
            root.append(res)
        else:
            low, high = recherche(P, low, high)
            if low != None:
                r = dichotomie(P, low, high)
                res = round(r, 2)
                P = oa.division(P,[F(-res), F(1)])[0]
                bases.unitaire(P)
                root.append(res)
    return root

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    print "test de bonus() :"

    # Test avec Q = [F(8),F(-20),F(-4),F(24)] 
    print "\n\nAvec le polynome Q de l'exercice precedent, on a:"
    res = bonus([F(8),F(-20),F(-4),F(24)])
    if sorted(res) == [-1.0, 0.5, 0.67]:
        test = "OK"
    else:
        test = "NOK" 
    print "bonus({})\nDes valeurs approchees des racines du polynome sont :".format([F(8),F(-20),F(-4),F(24)]),
    for i in res:
        print i,
    print
    print "Resultat attendu : -1.0 0.5 0.67"
    print " ---> test {}".format(test)

    # Test avec [F(625), F(-50), F(1)] : 25 racine double 
    res = bonus([F(625), F(-50), F(1)])
    if sorted(res) == [25,25]:
        test = "OK"
    else:
        test = "NOK" 
    print "\nbonus({})\nDes valeurs approchees des racines du polynome sont :".format([F(625), F(-50), F(1)]),
    for i in res:
        print i,
    print
    print "Resultat attendu : 25 25"
    print " ---> test {}".format(test)

    # Test avec [F(183), F(-104.2), F(-12.85), F(7.6), F(1)] : -6.1 -6 2.5 2
    res = bonus([F(183), F(-104.2), F(-12.85), F(7.6), F(1)])
    if sorted(res) == [-6.1, -6, 2, 2.5]:
        test = "OK"
    else:
        test = "NOK" 
    print "\nbonus({})\nDes valeurs approchees des racines du polynome sont :".format([F(183), -104.2, -12.85, 7.6, F(1)]),
    for i in res:
        print i,
    print
    print "Resultat attendu : -6.1 -6 2 2.5"
    print " ---> test {}".format(test)

    # Test avec [F(-1000), F(90), F(1)] : -100 10
    res = bonus([F(-1000), F(90), F(1)])
    if sorted(res) == [-100, 10]:
        test = "OK"
    else:
        test = "NOK" 
    print "\nbonus({})\nDes valeurs approchees des racines du polynome sont :".format([F(-1000), F(90), F(1)]),
    for i in res:
        print i,
    print
    print "Resultat attendu : -100 10"
    print " ---> test {}".format(test)

    # Test avec [F(-25100), F(1259), F(115.1), F(1)] : -100 -25.1 10
    res = bonus([F(-25100), F(1259), F(115.1), F(1)])
    if sorted(res) == [-100, -25.1, 10]:
        test = "OK"
    else:
        test = "NOK" 
    print "\nbonus({})\nDes valeurs approchees des racines du polynome sont :".format([F(-25100), F(1259), 115.1, F(1)]),
    for i in res:
        print i,
    print
    print "Resultat attendu : -100 -25.1 10"
    print " ---> test {}".format(test)
