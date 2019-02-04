# -*- coding: utf-8 -*-

import numpy as np
from timeit import Timer

li = list(range(500000))
nump_arr = np.array(li)

def python_for():
    return [num + 1 for num in li]

def numpy_add():
    return nump_arr + 1

python_timer=min(Timer(python_for).repeat(10, 10))
numpy_timer=min(Timer(numpy_add).repeat(10, 10))
times_faster=python_timer/numpy_timer
print(python_timer)
print(numpy_timer)
print(times_faster)
