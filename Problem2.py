# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 20:48:09 2018
@author: Adam

Project Euler
Problem #2
Even Fibonacci Numbers
"""
sum = 0
num1 = 0
num2 = 1
num3 = 0
limit = 4000000

while num3 < limit:
    if num3%2 == 0:
        sum += num3
    num3 = num1 + num2
    num1 = num2
    num2 = num3

print(sum)