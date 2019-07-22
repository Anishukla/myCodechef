# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:11:44 2019
@author: anishukla
"""

T = int(input())

for i in range(T):
    N, Z = input().split()
    N = int(N)
    Z = int(Z)
    L = list(map(int, input().split()))
    
    for k in range(Z):
        j = 0
        d = 0
        while(j<N-1):
            if(L[j] == 0 and L[j+1] == 1):
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
                j = j+2
                d = d+1
            else:
                j = j+1
                continue
            
        if(d == 0):
            break
            
    print(*L)
