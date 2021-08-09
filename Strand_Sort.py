'''

[4, 2, 5, 1, 3] -----> [4,2,5,1,3]------>[4, 5]
   S=4                                  list as l1
                                            |
                                            |
[1]<------[2, 3]<------[2, 1, 3]<-------[2, 1, 3]
 S=1      list as l2                       S=2

Merge L1 and L2
------>[2, 3, 4, 5] --------->[1, 2, 3, 4, 5]


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


def merge_list(a, b):
    out = []
    while len(a) and len(b):
        if a[0] < b[0]:
            out.append(a.pop(0))

        else:
            out.append(b.pop(0))

    out += a
    out += b
    print(out)
    return out


def strand(l):
    i, s = 0, [l.pop(0)]
    while i < len(l):
        if l[i] > s[-1]:
            s.append(l.pop(i))
        else:
            i += 1
    return s


def strand_sort(l):
    out = strand(l)
    while len(l):
        out = merge_list(out, strand(l))
    return out


ARRAY_LENGTH = 10000
# l = random.sample(range(0, 8000), 100)
l = input('Enter the list of numbers: ').split()   # USe Input..
l = [int(x) for x in l]
print(l)
strand_sort(l)
print(l)

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
run_sorting_algorithm(algorithm="sorted", array=array)
