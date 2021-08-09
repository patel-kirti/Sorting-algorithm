'''

[17, 3, 9, 1, 8]

comparsion :
3<17 ? yes. it swap     [3, 17, 9, 1, 8]

comparsion :
9<17 ? yes. it swap
9<3 ? no.                [3, 9, 17, 1, 8]

comparsion :
1<17 ? yes. it swap
1<9 ? yes. it swap       [1, 3, 9, 17, 8]
1<3 ? yes. it swap

comparsion :
8<17 ? yes. it swap
8<9 ? yes. it swap       [1, 3, 8, 9, 17]
8<3 ? no

Sorted list - [1, 3, 8, 9, 17]

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


def shell_sort(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap, size):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap = gap//2


# arr = random.sample(range(0, 8000), 100)  # Random generate list..
ARRAY_LENGTH = 10000

arr = input('Enter the list of numbers: ').split()   
arr = [int(x) for x in arr]
shell_sort(arr)
print('Sorted list: ', end='')
print(arr)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)
