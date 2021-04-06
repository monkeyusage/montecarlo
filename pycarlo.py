from cProfile import run
from carlolib.algorithm import np_random_walk, nb_random_walk, c_random_walk
import matplotlib.pyplot as plt

nb_random_walk(10000) # trigger jit compilation for fair comparison

# run("np_random_walk(1_000_000)") #=> runs in |27   | seconds
run("nb_random_walk(1_000_000)") #=> runs in | .11 | seconds
run("c_random_walk(1_000_000)")  #=> runs in | .035| seconds
