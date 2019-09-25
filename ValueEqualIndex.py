# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:40:17 2019

@author: Fahad
"""
def binarySearch(arr, low, high): 
    if high >= low: 
        mid = (low + high) // 2
      
    if mid == arr[mid]: 
        return mid 
      
    if mid > arr[mid]: 
        return binarySearch(arr, (mid + 1), high) 
    else: 
        return binarySearch(arr, low, (mid -1)) 
      
    # Return -1 if there is no Fixed Point 
    return -1
  
  
# Driver program to check above functions */ 
arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100] 
n = len(arr) 
print("Fixed Point is " + str(binarySearch(arr, 0, n-1)))