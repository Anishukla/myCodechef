# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:51:04 2019
@author: anishukla
"""

T = int(input())
while(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, None)
    loc = None
    for i in range(1, N+1):
        req = sum([int(b/(a+1)) for a, b in enumerate(A[i:N+1])])
        if(req <= K):
            loc = i
            break
    l = len(A)
    if(loc == None):
        loc = N+1
    print(loc)
    T = T-1
