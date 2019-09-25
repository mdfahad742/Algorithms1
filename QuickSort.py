# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 21:32:27 2019

@author: Fahad
"""
import random
def partition(L, l, r):
    
#    mid = (r + l) // 2
#        
#    if L[r] <= L[mid] and L[mid] <= L[l] or L[l] <= L[mid] and L[mid] <= L[r]:
#        p = mid
#    elif L[mid] <= L[r] and L[r] <= L[l] or L[l] <= L[r] and L[r] <= L[mid]:
#        p = r
#    else:
#        p = l
#        
#    print(L[r], L[mid], L[l], L[p])
    p = random.randrange(l, r + 1, 1)
    L[p], L[l] = L[l], L[p]
    pivot = L[l]
    #print("pivot", pivot)
    i = l + 1
    j = l + 1
    while(j <= r):
        if L[j] < pivot:
            L[j], L[i] = L[i], L[j]
            i += 1

        j += 1
    L[i - 1], L[l] = L[l], L[i - 1]
    return i - 1

def quickSelect(L, k):
    l = 0
    r = len(L) - 1
    while r > l:
        #print("L before", L)
        p = partition(L, l, r)
        #print("L after", L)
        #print("p", p)
        
        if p < k:
            l = p + 1
        elif p > k:
            r = p - 1
        else:
            return L[k]
    return L[k]

def R1Select(L, l, r, i):
    if l == r:
        return L[r]
    #print("L before", L)
    j = partition(L, l, r)
    #print("L after", L)
    #print("p", p)
    
    if j == i:
        return L[i]
    elif j > i:
        return R1Select(L, l, j - 1, i)
    else:
        return R1Select(L, j + 1, r, i - j)


def RSelect(L, l, r, i):
    if l == r: #and l == i:
        return L[l]
    #print("L before", L)
    j = partition(L, l, r)
    #print("L after", L)
    #print("j", j)
    
    if j == i:
        return L[i]
    elif j > i:
        return RSelect(L, l, j - 1, i)
    else:
        return RSelect(L, j + 1, r, i - j)
 


def quickSort(L, l, r):
    if l < r:
        p = partition(L, l, r)
        quickSort(L, l, p - 1)
        quickSort(L, p + 1, r)
    else:
        return
print("Enter the list:")
#L = [int(i) for i in open('QS.txt', 'r')]
L = [6, 5, 7, 9, 1, 2, 4, 8, 3]
count = len(L) - 1
#quickSort(L, 0, count)
for i in range(len(L)):
    #print(quickSelect(L, i))
    print(R1Select(L, 0, len(L) - 1, i))
    #print('ans', quickSelect(L, i))
print(L)

