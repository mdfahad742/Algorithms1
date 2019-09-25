# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:29:08 2019

@author: Fahad
"""

def matrix_multiplication(M, N, m1, n1, m2, n2): 
    
    R = [[0] * n2 for  i in range(m1)]
    print(R)
    for i in range(0, m1):  
        for j in range(0, n2):
            #R[i][j] = 0
            for k in range(0, n1):  
                R[i][j] += M[i][k] * N[k][j]
    for i in range(0, m1):  
        for j in range(0, n2):  
            print(R[i][j], end=" ") 
        print("") 
  
# First matrix. M is a list 
M = [[1, 1, 1, 1],  
    [2, 2, 2, 2],  
    [3, 3, 3, 3], 
    [4, 4, 4, 4]] 
  
# Second matrix. N is a list 
N = [[1, 1, 1, 1],  
    [2, 2, 2, 2],  
    [3, 3, 3, 3], 
    [4, 4, 4, 4]]
# Call matrix_multiplication function
if len(M[0]) == len(N):
    matrix_multiplication(M, N, len(M), len(M[0]), len(N), len(N[0]))
else:
    print("Matrix multiplication not possoble")