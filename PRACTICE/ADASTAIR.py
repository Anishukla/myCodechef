# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:01:14 2019
@author: anishukla
"""

import math
T = int(input())
while(T > 0):
    count = 0
    N, K = [int(x) for x in input().split()]
    steps = [int(x) for x in input().split()] 
    steps.append(0)
    steps.sort()
    for i in range(N):
        val = (steps[i+1]-steps[i])/K
        val = math.ceil(val)
        count = count + val - 1
    print(count)
    T = T-1