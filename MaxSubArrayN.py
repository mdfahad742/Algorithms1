# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 15:11:14 2019
@author: Fahad
Kadane's Algorithm
Dynamic Programming
"""
def maxSubArraySum(a,size):
	maxSum =a[0]
	curr_max = a[0]
	for i in range(1, size):
		curr_max = max(a[i], curr_max + a[i])
		maxSum = max(maxSum,curr_max)
	return maxSum
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is", maxSubArraySum(a,len(a)))