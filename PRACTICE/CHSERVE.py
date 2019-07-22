# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:00:12 2019
@author: anishukla
"""

T = int(input())

while(T>0):
    P1, P2, K = input().split()
    P1 = int(P1)
    P2 = int(P2)
    K = int(K)
    n = int(((P1 + P2)/K)%2)
    if n == 0:
        print("CHEF")
    elif n == 1:
        print("COOK")

    T = T - 1