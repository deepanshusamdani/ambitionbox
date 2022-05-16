"""
https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/and-operation-3-0b1a025c/
"""

"""
def And_Queries(Arr, V, L,N,Q,R):
    out = Arr
    for i in range(Q):
        for j in range(L[i],R[i]+1,1):  
            out[j-1] = out[j-1] & V[i]
    return out

N,Q = map(int, input().split())
Arr = list(map(int, input().split()))
L,R,V = [],[],[] 
for i in range(Q):
    T1,T2,T3 = map(int, input().split())
    L.append(T1)
    R.append(T2)
    V.append(T3)
out_ = And_Queries(Arr, V, L,N,Q,R)
print(' '.join(map(str,out_)))
"""


import numpy as np
N= 5 #length/size of array
Q= 2 #number of task
arr = [7,7,7,7,7]
# Q1= [1,3,4]
# Q2= [1,5,6]
L,R,V = 1,3,4

b=[]
for i in arr:
    b.append(bin(i).replace("0b", ""))

b = [int(i) for i in b]
print("b: ",b)
task1 = {}
for i in range(L-1,R,1):
    task1.update({i:bin(V).replace("0b", "")})

temp = list(task1.keys())
print(temp)    
for j in range(0,N):
    if j not in temp:
        print("j: ",j)
        task1.update({j:b[j]})
print("task: ",task1)
task1 = list(task1.values())
task1 = [int(i) for i in task1]
print("task1: ",task1)
print("type: ",type(task1))
res = []
for i in range(N):
    print("i: ",i)
    res.append(b[i] & task1[i])
print(res)

l = [1,1]
r = [3,5]
for i in range(Q):
    print("i: ",i)
    for j in range(l[i-1],r[i-1],1):
        print("j: ",j)
