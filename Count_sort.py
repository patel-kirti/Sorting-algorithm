from random import randint
from timeit import repeat
import random


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def CountSort(list):
    size = len(list)
    output = [0]*size
    count = [0]*10
    for i in range(0, size):
        count[list[i]] += 1
        
    for j in range(1, 10):
        count[j] += count[j-1]
    a = size-1
    
    while a >= 0:
        output[count[list[a]]-1] = list[a]
        count[list[a]] -= 1
        a -= 1
        
    for k in range(0, size):
        list[k] = output[k]


ARRAY_LENGTH = 10000
# list = random.sample(range(0, 8000), 100)  # Random generate list..

list = input('Enter the list of numbers: ').split()  # User Input...
list = [int(x) for x in list]
CountSort(list)
print('Sorted list: ', end='')
print(list)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)
