'''

[34, 10, 64, 51, 32, 21]     |   No. of Shifting to right
-------------------------------------------------------------------         
                             |
[34, 10, 64, 51, 32, 21]     |   Nothing
                             |
[10, 34, 64, 51, 32, 21]     |   34
                             |
[10, 34, 64, 51, 32, 21]     |   Nothing
                             |
[10, 34, 51, 64, 32, 21]     |   64
                             |
[10, 32, 34, 51, 64, 21]     |   34, 51, 64
                             |
[10, 21, 32, 34, 51, 64]     |   32, 34, 51, 64
                             
                             
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


def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    l_ind = r_ind = 0

    while len(result) < len(left) + len(right):
        if left[l_ind] <= right[r_ind]:
            result.append(left[l_ind])
            l_ind += 1
        else:
            result.append(right[r_ind])
            r_ind += 1

        if r_ind == len(right):
            result += left[l_ind:]
            break
        if l_ind == len(left):
            result += right[r_ind:]
            break
    return result


def merge_sort(l):
    if len(l) < 2:
        return l
    mp = len(l) // 2
    return merge(left=merge_sort(l[:mp]), right=merge_sort(l[mp:]))


def insertion_sort(l, left=0, right=None):
    if right is None:
        right = len(l) - 1

    for i in range(left+1, right+1):
        key = l[i]
        j = i-1
        while j >= left and l[j] > key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l


def timsort(l):
    min_run = 100
    n = len(l)

    for i in range(0, n, min_run):
        insertion_sort(l, i, min((i+min_run-1), (n-1)))

        size = min_run
        while size < n:
            for s in range(0, n, size*2):
                mid = s + size-1
                end = min((s+size*2-1), (n-1))

                merged = merge(left=l[s:mid+1], right=l[mid+1:end+1])

                l[s:s+len(merged)] = merged

        size *= 2
    return l


ARRAY_LENGTH = 10000
# l = random.sample(range(0, 8000), 100)  # Random generate list..

l = input('Enter the list of numbers: ').split()   # User Input
l = [int(x) for x in l]

timsort(l)
print('Sorted list: ', end='')
print(l)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)
