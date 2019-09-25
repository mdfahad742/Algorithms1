# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 15:23:13 2019

@author: Fahad
Divide and Conquer Approach
"""
 
def maxCrossingSum(left_arr, right_arr) : 
    
    sm = 0; left_sum = -10000
    
    for j in range(len(left_arr)) :
        i = len(left_arr) - j - 1
        sm = sm + left_arr[i] 
        
        if (sm > left_sum) : 
            left_sum = sm 
    
    
    sm = 0; right_sum = -1000
    for i in range(len(right_arr)) : 
        sm = sm + right_arr[i] 
        
        if (sm > right_sum) : 
            right_sum = sm 
    
 
    return left_sum + right_sum


def maxSubArraySum(arr) : 
    
    if len(arr) <= 1: 
        return arr[0]

    else:
        mid = len(arr) // 2

        # Return maximum of following three possible cases 
        # a) Maximum subarray sum in left half 
        # b) Maximum subarray sum in right half 
        # c) Maximum subarray sum such that the 
        #     subarray crosses the midpoint 
        left = maxSubArraySum(arr[ : mid])
        right = maxSubArraySum(arr[mid : ])
        cross_sum = maxCrossingSum(arr[ : mid], arr[mid : ])
        return max(left, right, cross_sum)          
 
arr = [-2, -3, 4, -1, -2, 1, 5, -3] 


max_sum = maxSubArraySum(arr) 
print("Maximum contiguous sum is ", max_sum) 
