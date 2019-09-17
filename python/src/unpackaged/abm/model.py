# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:04:46 2019

@author: gyral
"""
import random
y0 = 50
x0 = 50

random_number_y = random.random()

if random_number_y < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
random_number_x = random.random()

if random_number_x < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1

print(y0, x0)



y1 = 50
x1 = 50

random_number_y1 = random.random()

if random_number_y1 < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
    
random_number_x1 = random.random()

if random_number_x1 < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1

print(y1, x1)


result = (((y0-y1)**2) + ((x0-x1)**2))**0.5
print(result)