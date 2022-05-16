"""
https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/the-normal-type/
"""
from collections import defaultdict
import itertools
l = [1,2,2,1,1]
dd = defaultdict(list)
for i in range(1,len(l)+1):
    for j in range(i):
        dd[j,i].append(l[j:i])
ddd = dict(dd)
out = [x for x in itertools.product(*ddd.values())]
hh=[i for i in out[0]]
hh.sort()
new =  []
for i in range(1,len(hh)):
        if len(set(hh[i])) > 1:
            new.append(hh[i])
xx=[]
for i in ddd:
    if ddd[i][0] in new:
        xx.append(i)
cnt = len(xx)
print(cnt)