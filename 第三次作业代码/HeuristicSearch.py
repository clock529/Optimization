# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import copy

def test_conflict(arr, num, row, col):
    for i in range(9):
        if i != row and num == arr[i][col]:
            return False
        if i != col and num == arr[row][i]:
            return False
    for i in range(row//3 * 3, row//3 * 3 + 3):
        for j in range(col//3 * 3, col//3 * 3 + 3):
            if((i != row or j != col) and num == arr[i][j]):
                return False
    return True


def count(arr, row, col):
    n = 0
    num_list = []
    for num in range(1, 10):
        if (test_conflict(arr, num, row, col)):
            n = n + 1
            num_list.append(num)
    return n, num_list

def complete(a):
    for i in range(9):
        for j in range(9):
            if (a[i][j] == 0):
                return False
    return True
'''
def shudu(a, iter_num):
    if(complete(a)):
        print(a)
        return
    iter_num = iter_num + 1
    for row in range(9):
        for col in range(9):
            if (a[row][col] == 0):
                n, num_list = count(a, row, col)
                if(n == 0):
                    minIndex = index.index(min(index))
                    a = result[minIndex]
                    del(result[minIndex])
                    del(index[minIndex])
                    shudu(a, iter_num)
                else:
                   for num in num_list:
                        b = copy.deepcopy(a)
                        b[row][col] = num
                        result.append(b)
                        index.append(n+iter_num)
    minIndex = index.index(min(index))
    a = result[minIndex]
    del(result[minIndex])
    del(index[minIndex])
    shudu(a, iter_num)
    return
'''

def shudu(a, iter_num):
    if(complete(a)):
        print(a)
        return
    iter_num = iter_num + 1
    min_n = 10
    for row in range(9):
        for col in range(9):
            if (a[row][col] == 0):
                n, num_list = count(a, row, col)
                if(n == 0):
                    minIndex = index.index(min(index))
                    a = result[minIndex]
                    del(result[minIndex])
                    del(index[minIndex])
                    shudu(a, iter_num)
                    return
                elif n < min_n:
                        min_n = n
                        min_row = row
                        min_col = col
                        min_num_list = num_list.copy()
    for num in min_num_list:
        b = copy.deepcopy(a)
        b[min_row][min_col] = num
        result.append(b)
        index.append(min_n+iter_num)
    minIndex = index.index(min(index))
    a = result[minIndex]
    if(len(result) == 0):
        print('false')
        return 0
    del(result[minIndex])
    del(index[minIndex])
    shudu(a, iter_num)
    return

a = [[8, 0, 9, 7, 0, 5, 0, 0, 6],
     [0, 0, 6, 0, 0, 0, 7, 0, 0],
     [0, 0, 0, 0, 6, 0, 0, 0, 8],
     [0, 7, 0, 0, 2, 4, 8, 0, 0],
     [0, 0, 0, 0, 8, 0, 0, 0, 0],
     [0, 0, 5, 9, 7, 0, 0, 3, 0],
     [3, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 2, 0, 0, 0, 5, 0, 0],
     [9, 0, 0, 2, 0, 6, 3, 0, 1]]

result = []
index = []
iter_num = 0

shudu(a, iter_num)

                

