# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 03:08:36 2019

@author: Fahad
"""

def getInvCount(arr, n): 
  
    inv_count = 0
    for i in range(n - 1): 
        for j in range(i + 1, n): 
            if arr[i] > arr[j]: 
                inv_count += 1
  
    return inv_count 
 
print("Enter the list:")
arr = [int(i) for i in input().split(" ")] 
n = len(arr) 
print("Number of inversions are", getInvCount(arr, n))