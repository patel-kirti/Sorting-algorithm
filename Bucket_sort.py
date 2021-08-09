from random import randint
from timeit import repeat
import random


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def Bucket_sort(list, n):
    max_ele = max(list)
    min_ele = min(list)

    rng = (max_ele-min_ele)/n
    temp = []

    for i in range(n):
        temp.append([])

    for i in range(len(list)):
        diff = (list[i]-min_ele)/rng-int((list[i]-min_ele)/rng)
        if diff == 0 and list[i] != min_ele:
            temp[int((list[i]-min_ele)/rng)-1].append(list[i])
        else:
            temp[int((list[i]-min_ele)/rng)].append(list[i])

    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()

    k = 0
    for l in temp:
        if l:
            for i in l:
                list[k] = i
                k = k+1


ARRAY_LENGTH = 10000
# list=random.sample(range(0,8000),100)  # Random generated list
list = input('Enter the list of numbers: ').split()   
list = [int(x) for x in list]
n = 5
Bucket_sort(list, n)
print(list)


array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)
