# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:58:19 2019
@author: anishukla
"""

T = int(input())
while(T>0):
    N = int(input())
    
    BIT = 0
    NIBBLE = 0
    BYTE = 0
    
    if N%26 == 0:
        na = int(N/26)
        BYTE = int(2 ** (na-1))
    
        
    elif N%26 != 0:
        if 2 < N%26 < 11:
            nb = int(N/26)
            NIBBLE = int(2 ** (nb))
        elif 10 < N%26 < 26:
            nc = int(N/26)
            BYTE = int(2 ** (nc))
        elif 0 < N%26 < 3:
            nd = int(N/26)
            BIT = int(2 ** (nd))
    
    print(BIT, NIBBLE, BYTE)
    T=T-1    
    
    
