# function to generate all the sub lists
from typing import DefaultDict


def sub_lists (l):
    ll = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            ll.append(l[j: i])
    return ll
l1 = [1, 2, 3]
print(sub_lists(l1)) #output: [[1], [1, 2], [2], [1, 2, 3], [2, 3], [3]]
#------------------------------------------------------------------------------------------------

#print sum of sublist inside main list
ll= [[1], [1, 2], [2], [1, 2, 3], [2, 3], [3]]
k = [sum(l) for l in ll]
print(k)  # [1,3,2,6,5,3]
#------------------------------------------------------------------------------------------------

#find the max element of list and index
k = [1,3,2,6,5,3]
max = max(k)
ind = k.index(max)
#------------------------------------------------------------------------------------------------

#pair all possible element of list as sublist in main list:
test_list = [1, 7, 4, 3]
res = [(a, b) for idx, a in enumerate(test_list) for b in test_list[idx + 1:]]
print(res) #out: [(1, 7), (1, 4), (1, 3), (7, 4), (7, 3), (4, 3)]

#another method--
e = list(itertools.combinations(test_list,2))
#------------------------------------------------------------------------------------------------

#possible pair of list items to store with index using dictionary
from collections import defaultdict
l = [1,2,2,1,1]
dd = defaultdict(list)
for i in range(1,len(l)+1):
    for j in range(i):
        dd[j,i].append(l[j:i])
ddd = dict(dd)

#------------------------------------------------------------------------------------------------
import itertools
out = [x for x in itertools.product(*ddd.values())]
#here output of out is  list inside tuple like: [([1],[1,1],[1,2,2])]
hh=[i for i in out[0]]  #output: [[1],[1,1],[1,2,2]]
hh.sort()
#------------------------------------------------------------------------------------------------
new =  []
for i in range(1,len(hh)):
        if len(set(hh[i])) > 1:
            new.append(hh[i])
# if hh[i] != hh[i+1]:
# if len(set(hh[i])) >1:

xx=[]
for i in ddd:
    if ddd[i][0] in new:
        xx.append(i)
cnt = len(xx)
#------------------------------------------------------------------------------------------------

#convert the tuple of sublist-list of main list to "list" of sublist inside main:
#i/p:  
q = [(2, 4, 2), (2, 4, 3), (2, 4, 1), (2, 2, 3), (2, 2, 1), (2, 3, 1), (4, 2, 3), (4, 2, 1), (4, 3, 1), (2, 3, 1)]
e=[] 
size=3
for i in q:
    for j in i:
        e.append(j)
print(e) #output: [2, 4, 2, 2, 4, 3, 2, 4, 1, 2, 2, 3, 2, 2, 1, 2, 3, 1, 4, 2, 3, 4, 2, 1, 4, 3, 1, 2, 3, 1]

# now to make the sublist from given list element of same size
ww = [e[i:i+size] for i in range(0,len(e),size)]
print(ww) #output: [[2, 4, 2], [2, 4, 3], [2, 4, 1], [2, 2, 3], [2, 2, 1], [2, 3, 1], [4, 2, 3], [4, 2, 1], [4, 3, 1], [2, 3, 1]]

#---------------------------------------------------------------------------------------------------------

#for given list to create the equal size of sublist in main for each index
# i/p
a =[2,4,2,3,1] 
q = list(itertools.combinations(a, 3))
print(q) #output:[(2, 4, 2), (2, 4, 3), (2, 4, 1), (2, 2, 3), (2, 2, 1), (2, 3, 1), (4, 2, 3), (4, 2, 1), (4, 3, 1), (2, 3, 1)]

#---------------------------------------------------------------------------------------------------------

#find maximum for each sublist in main
a = [(2, 4, 2), (2, 4, 3), (2, 4, 1), (2, 2, 3), (2, 2, 1), (2, 3, 1), (4, 2, 3), (4, 2, 1), (4, 3, 1), (2, 3, 1)]
b = [max(p) for p in a]
print(b) #output: [4, 4, 4, 3, 2, 3, 4, 4, 4, 3]
#---------------------------------------------------------------------------------------------------------
seq=[1,2,3,4,5,6,7,8]
out = list(itertools.izip_longest(*[iter(seq)]*3))
#Out[20]: [(1, 2, 3), (4, 5, 6), (7, 8, None)]
#---------------------------------------------------------------------------------------------------------

arr= [1,2,3]
n = len(arr)
def bubble_sort(arr,n):
    flag = True
    cnt = 0
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False
                print("arr: ",arr)
        if flag:
            break
    return arr
bubble_sort(arr,n)
#-------------------------------------------------------------------------------------------------
g = [19,21]
k = [list(map(int,str(i))) for i in g]
print(k) #output: [[1,9],[2,1]]
#-------------------------------------------------------------------------------------------------

#second largest element of list-
List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
 
# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)
 
# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)
 
print(res)
#------------------------------------------------------------------------------------------------