#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 03:26:15 2019

@author: fahad
"""
m = 10 ** 9 + 7
T = int(input())
while T > 0:
    #N_L, L = [ int(i) for i in input().strip().split(" ")]
    #N_R, R = [ int(i) for i in input().strip().split(" ")]
    R = int(input())
    sum_x = 0
    for i in range(1, R + 1):
        s = str(i)
        s1 = "" + s[0]
        len_s = len(s)
        for i in range(len_s - 1):
            if s[i] != s[i + 1]:
                s1 += s[i + 1]
            else:
                s1 += '0'
        #print(s1)
        sum_x = (sum_x % m + int(s1) % m) % m
    print(sum_x)
    T = T - 1