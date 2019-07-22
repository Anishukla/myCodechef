# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:30:28 2019
@author: anishukla
"""

N, r = input().split()
N = int(N)
r = float(r)
the_list = []
for i in range(N):
    R = float(input()) 
    the_list.append(R) 
for j in range(N):    
    if(the_list[j]>=r):
        print("Good boi")
    elif(r>the_list[j]):
        print("Bad boi")