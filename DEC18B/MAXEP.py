# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:44:27 2019
@author: anishukla
"""

N, c = input().split()
N = int(N)
c = int(c)
amt = 1000
start = 1
end = N 
val = int((N+1)/2)
b = end - start  
done = False
k = amt//c
if(N == 1):
    print("3 1")

while(N != 1):
    if(k<0 or amt<0):
        break
    if done:
        break
    print(1, 1)
    u = int(input())
    if(u == 1):
        print(2)
        print(3, 1)
        k = k-1
        break
    
    print(1, N-1)
    u = int(input())
    if(u == 0):
        print(3, N)
        break
    if(u == 1):
        amt = amt - c
        amt = amt - 2
        k = k-1
        print(2)
    
    print(1, val)
    while(b != 1):
        u = int(input())
        
        if(u == -1):
            print(1, val)
            continue
            
        if(u == 0):
            if(k< 0 or amt<0):
                print(2)
                print(3, val+1)
                break
            b = end - start
            if(b == 1):
                print(3, val+1)
                done = True
                break
            start = val
            val = int((start + end)/2)
            amt = amt - 1
            print(1, val)
            
        elif(u == 1):
            k = k-1
            if(k<0 or amt<0):
                print(3, val + 1)
                break
            b = end - start
            if(b == 1):
                print(2)
                print(3, val+1)
                done = True
                break
            amt = amt - c
            print(2)
            end = val
            val = int((start + end)/2)
            amt = amt -1
            print(1, val)
