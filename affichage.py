# coding: utf-8

from fractions import Fraction as F


def affich(P):
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
    return poly
