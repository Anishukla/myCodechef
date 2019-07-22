# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:50:54 2019
@author: anishukla
"""

T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    lt = len(A)
    result = "Poor Chef"
    P = dict()
    for i in range(lt):
      new_value = A[A[i] - 1]
      M = P.get(new_value)
      if (M == None):
        P.update({new_value: i})
      else:
        if (A[M] != A[i]):
          result = "Truly Happy"
    print(result)