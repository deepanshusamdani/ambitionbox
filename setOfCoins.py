"""
https://www.hackerearth.com/problem/algorithm/magic-land-0c4e9fb0-77aa8eb6/
"""

import itertools
n,m = map(int, input().split())
a = list(map(int,input().split()))

comb = list(itertools.combinations(a,m))
maxE = [max(i) for i in comb]
tot = sum(maxE)
print(tot)


"""
input:

5 3
2 4 2 3 1
"""
"""
output:

35
"""