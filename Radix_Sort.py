'''
[23,234,43,65,898,0,12,2]
 
step-1 | step-2 | step-3 | step-4
       |        |        |
023    | 000    | 000    | 000
234    | 012    | 002    | 002
043    | 002    | 012    | 012
065    | 023    | 023    | 023
898    | 043    | 234    | 043
000    | 234    | 043    | 065
012    | 065    | 065    | 234
002    | 898    | 898    | 898

sorted element - [0, 2, 12, 23, 43, 65, 234, 898]

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

def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1    # increse count

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


def radixSort(array):
    max_element = max(array)

    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10                    # increse place 10,100,1000..n

ARRAY_LENGTH = 10000

# array=random.sample(range(0,800),100)
array = input('Enter the list of numbers: ').split()   # User Input
array = [int(x) for x in array]
n = 5
radixSort(array)
print(array)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)