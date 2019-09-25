# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 03:51:29 2019

Its not implemented efficiently due to slow exponentiation & not practical as number not taken as String.

@author: Fahad
"""
def multiplication(x, y):
    if x < 10 and y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n // 2
        a = x // (10 ** nby2)
        b = x % (10 ** nby2)
        c = y // (10 ** nby2)
        d = y % (10 ** nby2)
        
        ac = multiplication(a, c)
        bd = multiplication(b, d)
        ad_plus_bc = multiplication(a + b, c + d) - ac - bd
        
        return (10 ** (nby2 * 2) * ac) + (10 ** (nby2) * ad_plus_bc) + bd



x = int(input())
y = int(input())
print("The multiplacation of " + str(x) + " and " + str(y) + " is " + str(multiplication(x, y)))