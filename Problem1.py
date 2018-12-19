# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:29:32 2018
@author: Adam

Project Euler
Problem #1
Multiples of 3 and 5

sum_1 for my solution
sum_2 for given more efficient solution (not finished)
"""
i = 3
sum_1 = 0

for i in range(3,1000):
    if i%3 == 0 or i%5 == 0:
        sum_1 += i
    
print(sum_1)

