# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:51:39 2019
@author: anishukla
"""

N, Q, K = input().split()
Q = int(Q)
K = int(K)
A = list(map(int, input().split()))
B = ''.join(map(str, A))
inp = input()

for i in range(Q):
    if(inp[i] == '!'):
        A = [A[-1]] + A[:-1]
        B = ''.join(map(str, A))
    
    elif(inp[i] == '?'):
        res = max(map(len, B.split('0')))
        print(min(K, res))