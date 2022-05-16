"""
Input array [1,3,2,7] so basically this array represents the number 1327. 
All the possible combinations are : 
1. [3 1 2 7] get by swapping indices 1 and 2. 
2. [2 3 1 7] get by swapping indices 1 and 3. 
3. [7 3 2 1] get by swapping indices 1 and 4. 
4. [1 2 3 7] get by swapping indices 2 and 3. 
5. [1 7 2 3] get by swapping indices 2 and 4. 
6. [1 3 7 2] get by swapping indices 3 and 4. 
Out of all the possible combinations, 3 give the maximum number as 7321, so we will return [7 3 2 1].
"""
import copy
arr = [1,3,2,7]
a = copy.deepcopy(arr)
rev = arr[::-1]
s = []
s.append(rev)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        a[j],a[i] = a[i],a[j]
        s.append(a)
        a = copy.deepcopy(arr)
h =[]
for i in range(len(s)):
    h.append((int("".join(str(j) for j in s[i]))))
h.sort()
m = h[-1]
# m  = m.split(" ")
print("m: ",m)
        

