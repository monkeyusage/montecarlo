from __future__ import annotations
import numpy as np
from numba import njit
import os
import ctypes

def np_random_walk(steps):
    SQRT_STEPS = np.sqrt(steps)
    walk = np.ones(steps)
    for idx in range(steps):
        y = np.random.choice(np.array([-1, 1]))
        walk[idx] = walk[idx-1] + (y / SQRT_STEPS)
    return walk

@njit
def nb_random_walk(steps):
    SQRT_STEPS = np.sqrt(steps)
    walk = np.ones(steps)
    for idx in range(steps):
        y = np.random.choice(np.array([-1, 1]))
        walk[idx] = walk[idx-1] + (y / SQRT_STEPS)
    return walk

# conditional library loading
if os.name == "posix":
    algo = ctypes.cdll.LoadLibrary("carlolib/bin/algorithm.so")
else:
    algo = ctypes.cdll.LoadLibrary("carlolib/bin/algorithm.dll")

_random_walk = algo.random_walk
_random_walk.restype = ctypes.POINTER(ctypes.c_double)

def c_random_walk(steps: int) -> np.ndarray:
    ptr = _random_walk(ctypes.c_int(steps))
    arr = np.ctypeslib.as_array(ptr, (steps,)).copy()
    algo.free_arr(ptr) # clean up
    return arr