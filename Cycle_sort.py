from random import randint
from timeit import repeat
import random


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def cycle_sort(list1):
    writes = 0    # no. of cycles

    for c_start in range(0, len(list1)-1):
        item = list1[c_start]
        pos = c_start
        for i in range(c_start+1, len(list1)):
            if list1[i] < item:
                pos += 1

        if pos == c_start:
            continue

        while item == list1[pos]:
            pos += 1

        list1[pos], item = item, list1[pos]
        writes += 1

        while pos != c_start:
            pos = c_start
            for i in range(c_start+1, len(list1)):
                if list1[i] < item:
                    pos += 1
            while item == list1[pos]:
                pos += 1

            list1[pos], item = item, list1[pos]
            writes += 1


ARRAY_LENGTH = 10000

list1 = random.sample(range(0, 8000), 100)
# list1=input("Enter list :- ").split()
list1 = [int(x) for x in list1]
cycle_sort(list1)
print(list1)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)
