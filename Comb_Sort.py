'''

[5, 15, 37, 29, 25, 79] --------> [5, 15, 37, 29, 25, 79]
                                    Gap=4 No Change  Pairs = (5,25)(15,79)
                                            |
                                            |
                                            |
[5, 15, 25, 29, 37, 79] <-------- [5, 15, 37, 29, 25, 79]
  Gap=2 Swap(37,25)                   Gap=3 No Change  Pairs = (5,29)(15,25)(37,79)
  Pairs = (5,25)(15,29)(37,25)(29,79)     
       |
       |
       |                 
[5, 15, 25, 29, 37, 79] <-------- [5, 15, 25, 29, 37, 79] Sorted List
  Gap=1 no change                  
  Pairs = (5,15)(15,25)(25,29)(29,37)(37,79)     
                                   
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


def comb_sort(list1):
    n = 1.3
    gap = len(list1)
    swapp = True
    i = 0

    while gap > 1 or swapp:
        gap = int(float(gap)/n)

        swapp = False
        i = 0

        while gap+i < len(list1):
            if list1[i] > list1[i+gap]:
                list1[i], list1[i+gap] = list1[i+gap], list1[i]
                swapp = True
            i += 1
    return list1


# list1 = random.sample(range(0, 8000), 100)  # Random generate list..
ARRAY_LENGTH = 10000

list1 = input("Enter List :- ").split() 
list1 = [int(x) for x in list1]
comb_sort(list1)
print(list1)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)
