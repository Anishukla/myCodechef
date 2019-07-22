# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
def fast_pow(ttp, num):
    req = 1
    while(num > 0):
        if(num % 2 == 1):
            req = (req * ttp) % ref
        num = num // 2
        ttp = (ttp * ttp) % ref

    return req


ref= 10**9 + 7

T= int(input())
for i in range(T):
    K = int(input())
    
    val = fast_pow(2, (K-1))
    ans= val*10
    
    print(ans%ref)
