# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:50:05 2019

@author: My
"""
from numpy import *
import matplotlib.pyplot as plt

def init(chromnum, chromlen):
    return random.randint(0, 2, size = (chromnum, chromlen))

def func(pop):
    x = decode(pop)
    return multiply(x, sin(3 * x))

def decode(pop):
    n, l = pop.shape
    result = zeros((1, n))
    for i in range(l):
        result = result + pow(2, l - 1 - i) * pop[:, i]
    return result.T * 31/(pow(2, 22) - 1) - 1

def fitval(val):
    fit = val.copy()
    fit[val < 0] = 0
    return fit

def select(pop, fit):
    fit = cumsum(fit/sum(fit), axis = 0)
    n, l = pop.shape
    newpop = zeros((n, l))
    select_prob = random.random(size = (1, n))
    for i in range(n):
        for j in range(n):
            if select_prob[0, i] < fit[j]:
                newpop[i, :] = pop[j, :]
                break
    return newpop

def cross(pop, pc):
    n, l = pop.shape
    newpop = zeros((n, l))
    cross_prob = random.random(size = (1, n//2))
    cross_pos = random.randint(1, l-1, size = (1, n//2))
    random.shuffle(pop)
    for i in range(0, n, 2):
        if cross_prob[0, i//2] < pc:
            newpop[i, 0:cross_pos[0, i//2]] = pop[i, 0:cross_pos[0, i//2]]
            newpop[i, cross_pos[0, i//2]:] = pop[i+1, cross_pos[0, i//2]:]
            newpop[i+1, 0:cross_pos[0, i//2]] = pop[i+1, 0:cross_pos[0, i//2]]
            newpop[i+1, cross_pos[0, i//2]:] = pop[i, cross_pos[0, i//2]:]
        else:
            newpop[i, :] = pop[i, :]
            newpop[i+1, :] = pop[i+1, :]
    return newpop

def variation(pop, pm):
    n, l = pop.shape
    newpop = pop.copy()
    variation_prob = random.random(size = (1, n))
    variation_pos = random.randint(0, l, size = (1, n))
    for i in range(n):
        if variation_prob[0, i] < pm:
            newpop[i, variation_pos[0, i]] = 1 - pop[i, variation_pos[0, i]]
    return newpop

def best(pop, fit):
    n, l = pop.shape
    index = argmax(fit)
    best_pop = zeros((1, l))
    best_pop[0, :] = pop[index, :]
    best_x = decode(best_pop)
    return best_x, fit[index]

def limit(pop):
    x = decode(pop)
    pop[nonzero(x > 31)[0], :] = array([1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0])
    return pop

chromnum = 40
chromlen = 22
pc = 0.8
pm = 0.1
N = 1000
best_x = zeros((1, N))
best_fit = zeros((1, N))
ave_fit = zeros((1, N))
ave_fit2 = zeros((1, N))
ave_fit3 = zeros((1, N))
pop = init(chromnum, chromlen)

for i in range(N):
    val = func(pop)
    fit = fitval(val)
    best_x[0, i], best_fit[0, i] = best(pop, fit)
    ave_fit[0, i] = sum(fit)/chromnum
    pop = select(pop, fit)
    val2 = func(pop)
    fit2 = fitval(val2)
    ave_fit2[0, i] = sum(fit2)/chromnum
    pop = cross(pop, pc)
    val3 = func(pop)
    fit3 = fitval(val3)
    ave_fit3[0, i] = sum(fit3)/chromnum
    pop = variation(pop, pm)

plt.figure()
plt.plot(range(N), ave_fit2.T, label = 'ave_fit')

plt.plot(range(N), best_fit.T, label = 'best_fit', c = 'r', ls = '--')
plt.legend(loc = 'down right')
plt.show()

plt.figure()
plt.plot(range(N), best_x.T, label = 'best_x')
plt.show()
plt.figure()
plt.plot(range(N), ave_fit.T, 'b:', label = 'ave_fit_variation')

plt.plot(range(N), ave_fit2.T, 'g-.', label = 'ave_fit_select')
plt.plot(range(N), ave_fit3.T, 'r--',  label = 'ave_fit_cross')



plt.legend(loc = 'down right')

plt.figure()
plt.plot(range(N), ave_fit.T, 'b:', label = 'ave_fit_variation')

plt.plot(range(N), ave_fit2.T, 'g-.', label = 'ave_fit_select')
plt.plot(range(N), ave_fit3.T, 'r--',  label = 'ave_fit_cross')
plt.xlim(600, 800)  # 限定横轴的范围
plt.ylim(25, 30)  # 限定纵轴的范围

print(best_x[0, -1])