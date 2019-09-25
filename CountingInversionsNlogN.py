# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 04:24:03 2019

@author: Fahad
"""

def sort_and_count(L):
    if len(L) <= 1:
        return L[ : ], 0
    else:
        mid = len(L) // 2
        left, x = sort_and_count(L[ : mid])
        right, y = sort_and_count(L[mid : ])
        left_plus_right, z =  merge_and_countSplitInv(left, right)
        return left_plus_right, x + y + z
    
def merge_and_countSplitInv(left, right):
    i, j = 0, 0
    x = []
    count = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            x.append(left[i])
            i += 1
        else:
            x.append(right[j])
            j += 1
            count += len(left) - i
            
    while i < len(left):
        x.append(left[i])
        i += 1
    while j < len(right):
        x.append(right[j])
        j += 1 
    return x, count

print("Enter the list:")
L = [int(i) for i in input().split(" ")]
sorted_L, countInv = sort_and_count(L)
print("Number of inversions are", countInv)