# PROJET S2

**Overall objective :** To realize a set of functions allowing to perform exact calculations on the polynomials of Q[x]

## bases.py
Basic functions on polynomials

### deg
Return the degree of the polynomial given as input (will return -1 for the zero polynomial)

### unitaire
Transform the given input polynomial into a monic polynomial

### monome
Take as input an integer n and return the list corresponding to the monome X^n

## operations_elementaires.py

### somme
Return the sum of the two polynomials given as inputs

### diff
Return the difference between the first and second polynomial given as input

### produit
Return the product of the two polynomials given as input

## autres.py

### racine 
take as input a list of rationals of any length and return the list associated with the polynomial ![](https://latex.codecogs.com/gif.latex?\prod_{k=0}^n(X-a_{k}))

### evalue
Horner's algorithm

## operations_avancees.py

### puissance
Taking as input a list L representing a polynomial P and an integer n, the functionwill return P^n

### division
Taking as input two lists L1 and L2 representing two polynomials P1 respectively
and P2, the function will return the quotient and the rest of the Euclidean division of P1 by P2.

### pgcd
Return the PGCD of the two polynomials given as input

### derive
Return the derivative from the given input polynomial

## exercice.py
Solves and displays mathematical exercise.

## bonus.py
Calculate the real roots (approximate values) of a real polynomial
