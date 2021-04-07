from __future__ import annotations
from carlolib.algorithm import np_random_walk, nb_random_walk, c_random_walk
from time import time

def benchmark(func: function):
    multiple = 1
    for _ in range(8):
        t_0 = time()
        func(multiple)
        t_1 = time()
        multiple *= 10
        elapsed = t_1 - t_0
        print(f"{func.__name__}\t{elapsed}")

if __name__ == "__main__":
    nb_random_walk(100)
    for func in [np_random_walk, nb_random_walk, c_random_walk]:
        benchmark(func=func)
