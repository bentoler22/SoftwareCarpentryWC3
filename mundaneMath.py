# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:58:16 2019

@author: bento
"""

sum = 0
for i in range(1,100):
    if (i % 2) == 0:
        sum =sum + i
    else:
        sum = sum
print(sum)