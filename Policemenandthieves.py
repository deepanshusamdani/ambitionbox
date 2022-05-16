import itertools
def solution(A,k):
    i = 0
    l = 0
    r = 0
    res = 0
    thi = [] 
    pol = []
    
    arr= list(itertools.chain.from_iterable(A))
    n = len(arr)
    # print("n:",n)
    while i < n-1: 
        if arr[i] == 'P': 
            pol.append(i) 
        elif arr[i] == 'T': 
            thi.append(i) 
        i += 1
    while l < len(thi) and r < len(pol): 
        if (abs( thi[l] - pol[r] ) <= k): 
            res += 1
            l += 1
            r += 1
        elif thi[l] < pol[r]: 
            l += 1
        else: 
            r += 1
    return res

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(input().split())
    out_ = solution(A, K)
    print (out_)

"""
1
3 1
P T P
T P T
T T P
"""