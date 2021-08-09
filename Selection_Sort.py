from random import randint
from timeit import repeat
import random


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def SelectionSort(list):
    n = len(list)
    for i in range(n - 1):
        minvalue = i
        for j in range(i + 1, n):
            if list[j] < list[minvalue]:
                minvalue = j
        if minvalue != i:
            temp = list[i]
            list[i] = list[minvalue]
            list[minvalue] = temp
    return list


ARRAY_LENGTH = 10000
# list = random.sample(range(0, 8000), 100)  # Random generate list..

list = input('Enter the list of numbers: ').split()   
list = [int(x) for x in list]
SelectionSort(list)
print('Sorted list: ', end='')
print(list)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)
