from random import randint
from timeit import repeat
import random


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def merge_sort(list, left, right):
    if left >= right:
        return
    middle = (left+right)//2
    merge_sort(list, left, middle)
    merge_sort(list, middle+1, right)
    merge(list, left, right, middle)


def merge(list, left, right, middle):
    l1 = list[left:middle+1]
    r1 = list[middle+1:right+1]
    l_index = 0
    r_index = 0
    index = left
    while l_index < len(l1) and r_index < len(r1):
        if l1[l_index] <= r1[r_index]:
            list[index] = l1[l_index]
            l_index = l_index+1
        else:
            list[index] = r1[r_index]
            r_index = r_index+1
        index = index+1
    while l_index < len(l1):
        list[index] = l1[l_index]
        l_index = l_index+1
        index = index+1
    while r_index < len(r1):
        list[index] = r1[r_index]
        r_index = r_index+1
        index = index+1


ARRAY_LENGTH = 10000
list = random.sample(range(0, 8000), 100)  # Random generate list..

# list = input('Enter the list of numbers: ').split()    # User Input......
# merge_sort(list, 0, len(list)-1)
print(list)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)] 
run_sorting_algorithm(algorithm="sorted", array=array)
