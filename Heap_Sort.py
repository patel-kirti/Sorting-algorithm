from random import randint
from timeit import repeat
import random


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

def max_heapify(A, n, i):
    l = left(i)
    r = right(i)
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(A):
    n = len(A)
    for i in range(n, -1, -1):
        max_heapify(A, n, i)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, i, 0)

ARRAY_LENGTH=10000
# A = random.sample(range(0, 8000), 100)
A = input('Enter the list of numbers: ').split()   # User Input
A = [int(x) for x in A]
build_max_heap(A)
print(A)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)