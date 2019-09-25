#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 12:26:24 2019

@author: fahad
"""
import math

def b(n, k): 
    if(k > n - k): 
        k = n - k  
    res = 1
    for i in range(k): 
        res = res * (n - i) 
        res = res / (i + 1) 
    return res 

def primeFactors(n):
    sum_x = 0
    while n % 2 == 0: 
        sum_x += 2 
        n = n // 2
    for i in range(3, int(math.sqrt(n))+ 1, 2): 
        while n % i== 0: 
            sum_x += i
            n = n / i 

    if n > 2: 
        sum_x += n
    return sum_x
        

#k = int(input())
#A = [ int(i) for i in input().strip().split(" ")]
#print(getSubsets(k, len(A), A))
print(b(26, 13) - b(26, 14))
print(b(24, 12) - b(24, 13))
print(b(22, 11) - b(22, 12))
print(b(20, 10) - b(20, 11))