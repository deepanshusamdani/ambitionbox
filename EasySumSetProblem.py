"""
https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/easy-sum-set-problem-7e6841ca/
"""

import numpy as np
import pandas as pd
import itertools

n =2
m =3
a=[1,2]
c=[3,4,5]

b = set()
l = c[0] - a[0]
r = c[-1] - a[-1]

for i in range(l, r+1):
    found = True
    for k in range(n):
        if (a[k] + i) not in c:
            found = False
            break
    if found:
        b.add(i)
for element in sorted(b):
    print(element, end = " ")

 
