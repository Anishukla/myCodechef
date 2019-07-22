# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:43:20 2019
@author: anishukla
"""

import random
my_list = [1, 2, 3]
X = random.choice(my_list)
print(X)
Y = int(input())
if((X==1 and Y==2) or (X==2 and Y==1)):
    print("3")
elif((X==3 and Y==2) or (X==2 and Y==3)):
    print("1")
else:
    print("2")