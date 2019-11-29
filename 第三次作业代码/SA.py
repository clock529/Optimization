# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:16:59 2019

@author: My
"""
import random
import math
import matplotlib.pyplot as plt

def func(x):
    return -x * math.sin(3 * x)

def find(x, min_x, max_x):
    new_x = x + random.uniform(-3, 3)
    if new_x < min_x:
        new_x = min_x
    elif new_x > max_x:
        new_x = max_x
    return new_x

P0 = 0.8
delta_f = 10
T0 = 60
L = 1000
K = 600
alpha = 0.95
min_x = -1
max_x = 30
T = []
x = []
T.append(T0)
x.append(random.uniform(min_x, max_x))

for k in range(K):  
    temp = x[k]
    for l in range(L):
        f = func(temp)
        new_x = find(temp, min_x, max_x)
        new_f = func(new_x)
        if f > new_f:
            temp = new_x
        elif math.exp(-(new_f - f)/T[k]) > random.uniform(0, 1):
            temp = new_x
    x.append(temp)
    T.append(alpha * T[k])
print(x[K])
plt.figure()
plt.plot(range(K), x[0:K])
plt.xlabel('k')
plt.ylabel('x')
plt.show()
   