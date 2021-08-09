'''
[9,2,3,8,1,5,9]

max=9   min=1   range=max-min+1

index | 
 0    | 1           setp - 1 : 9-1= 8=> buk[8]
 1    | 2           setp - 2 : 2-1= 1=> buk[1]
 2    | 3           setp - 3 : 3-1= 3=> buk[3]
 3    |             setp - 4 : 8-1= 7=> buk[7]
 4    | 5           setp - 5 : 1-1= 1=> buk[0]
 5    |             setp - 6 : 5-1= 4=> buk[4]
 6    |             setp - 7 : 9-1= 8=> buk[8]
 7    | 8
 8    | 9 9
 
 sorted element - [1,2,3,5,8,9,9]
 
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



def pigeohole_sort(l):
    mini = min(l)
    maxi = max(l)
    size = maxi-mini+1   # calculate size

    holes = [0] * size
    for i in l:
        assert type(i) is int, "Integers are accepted"  # assert keyword of python it return true or false 
        holes[i-mini] +=1

    a = 0
    for c in range(size):
        while holes[c]>0:
            holes[c] -=1
            l[a] = c+mini
            a += 1

    return l

ARRAY_LENGTH=10000
# l=random.sample(range(0,8000),100)
l = input("Enter list :- ").split()
l = [int(x) for x in l]
pigeohole_sort(l)
print(l)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)
