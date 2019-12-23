# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:11:42 2019

@author: Liz
"""

count_letters = {}

def counter(input_string):
    for letter in input_string: 
        if letter in alphabet: 
            if letter in count_letters:
                count_letters[letter] += 1
            else: 
                count_letters[letter] = 1

address_count = count_letters

def rand():
    random.uniform(-1, 1)
    
x = (0, 0)
y = (1, 1)    
def distance(x, y):
    return math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)

def in_circle(x, origin = [0, 0]):
    if distance(x, origin) < 1:
        return True
    else: 
        return False

R = 10000
x = [(rand(), rand()) for i in range(R)]
inside = [in_circle(p) for p in x]
print(sum(inside) / R)

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    for i in range(0, n):
        return (sum(x[i:(i+width)]) / width)
x = [0,10,5,3,1,5]
print(moving_window_average(x, 1))

R = 1000
x = [random.uniform(0, 1) for i in range(R)]
Y = [x] + moving_window_average(x, n_neighbors) for n_neighbors in range(1, 10) 
print(len(Y))