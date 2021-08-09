from random import randint
from timeit import repeat
import random


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def QuickSort(list, low, high):
    if low < high:
        p = partition(list, low, high)
        QuickSort(list, low, p - 1)
        QuickSort(list, p + 1, high)


def partition(list, low, high):
    i = low - 1
    pivot = list[high]
    for j in range(low, high):
        if list[j] <= pivot:
            i = i + 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[high] = list[high], list[i + 1]
    return i + 1


ARRAY_LENGTH = 10000
# list = random.sample(range(0, 8000), 100)  # Random generate list..

list = input('Enter the list of numbers: ').split()  # User Input...
# n = len(list)
QuickSort(list, 0, len(list) - 1)

print("Sorted List :- ")
print(list)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)
