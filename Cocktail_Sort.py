''' 

[9, 7, 2, 5, 4, 1, 12,3] -----> [9, 7, 2, 5, 4, 1, 3, 12]
 ---------------------->         <------------------
   max=12                              min=1   
                                        |
                                        |
                                        |
[1, 7, 2, 5, 4, 3, 9, 12] <----- [1, 7, 2, 5, 4, 9, 3, 12]
    <------------                   ---------------->
    min=2                                max=9
       |
       |
       | 
[1, 2, 7, 5, 4, 3, 9, 12] <----- [1, 2, 3, 5, 4, 7, 9, 12]
       --------->                       <------
    max=7                              max=5
                                        |
                                        |
                                        |
                                [1, 2, 3, 4, 5, 7, 9, 12]  
                                        
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

def cocktail_sort(list1):

    for i in range(len(list1)-1, 0, -1):   # backword 
        swapp = False

        for j in range(i, 0, -1):  # backword loop  chack larger element to the left most part of list
            if list1[j] < list1[j-1]:
                list1[j], list1[j-1] = list1[j-1], list1[j]
                swapp = True

        for j in range(i):       # forword loop  chack larger element to the right most part of list
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
                swapp = True

        if not swapp:
            return list1

list1 = random.sample(range(0, 8000), 100)  # Random generate list..
ARRAY_LENGTH = 10000

# list1 = input("Enter list :- ").split()
list1 = [int(x) for x in list1]
cocktail_sort(list1)
print(list1)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)