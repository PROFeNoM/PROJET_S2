# coding: utf-8
 
import operations_elementaires as oe
import operations_avancees as oa
import autres as a
from math import factorial
from fractions import Fraction as F

def tcheb(n):
    T_0 = [1]
    T_1 = [0,1]
    for _i in range(n-1): 
        T_1, T_0 = oe.diff(oe.produit([0,2], T_1), T_0), T_1
    return T_1

def pascal(n):
    row = list()
    k = 0
    for _i in range(n+1):
        row.append(binomial(n, k))
        k+=1
    return row

def binomial(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))


if __name__ == "__main__":
    print(tcheb(10))
    print(pascal(15))
    P = [F(2),F(-7),F(-6),F(34),F(10),F(-63),F(-22),F(44),F(24)]
    P_der = oa.derive(P)
    print(P_der)
    pgcd = oa.pgcd(P, P_der)
    print(pgcd)
    for i in 
