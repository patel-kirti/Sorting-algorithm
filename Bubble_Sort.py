'''
l=[8, 2, 6, 4, 5]

swap 8 > 2
[2, 8, 6, 4, 5]

swap 8>6
[2, 6, 8, 4, 5]

swap 8>5
[2, 6, 4, 5, 8]

2<6
[2, 6, 4, 5, 8]

swap 6>4
[2, 4, 6, 5, 8]

swap 6>5
[2, 4, 5, 6, 8]

Sorted element - [2, 4, 5, 6, 8]

'''


from random import randint
from timeit import repeat
import random


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def bubble_sort(list1):
    has_swapped = True

    total_iteration = 0

    while(has_swapped):
        has_swapped = False
        for i in range(len(list1) - total_iteration - 1):
            if list1[i] > list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
                has_swapped = True
        total_iteration += 1
    print("The number of iteraton: ", total_iteration)
    return list1


ARRAY_LENGTH = 10000
# list1 = random.sample(range(0, 8000), 8000)  # Random generate list..

list1 = input('Enter the list of numbers: ').split()
list1 = [int(x) for x in list1]
bubble_sort(list1)
print('Sorted list: ', end='')
print(list1)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)
