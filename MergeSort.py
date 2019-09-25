# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:48:27 2019

@author: Fahad
"""

def mergeSort(L):
    if len(L) <= 1:
        return L[ : ]
    else:
        mid = len(L) // 2
        left = mergeSort(L[ : mid])
        right = mergeSort(L[mid : ])
        return merge(left, right)
    

def merge(left, right):
    i, j = 0, 0
    x = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            x.append(left[i])
            i += 1
        else:
            x.append(right[j])
            j += 1
            
    while i < len(left):
        x.append(left[i])
        i += 1
    while j < len(right):
        x.append(right[j])
        j += 1 
    return x



print("Enter the list:")
L = [int(i) for i in input().strip().split(" ")]
sorted_L = mergeSort(L)
print(sorted_L)