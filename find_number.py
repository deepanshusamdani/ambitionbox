import numpy as np
import itertools
# N,X,K= map(int, input().split())
# S = str(input())
N,X,K = 10,5,10
S= "1234567891"

new = []
for index in range(0, len(S), X):
    new.append(S[index : index + X])
out = [x for x in itertools.product(*new)]
def join_tuple_string(strings_tuple):
   return ''.join(strings_tuple)
final = list(map(join_tuple_string, out))
final.sort()
result = final[K-1]
print(result)









# s = [[a, b] for a in new for b in new]
# initializing the list with tuples
# string_tuples = [('A', 'B', 'C'), ('Tutorialspoint', 'is a', 'popular', 'site', 'for tech learnings')]

# # function that converts tuple to string
# def join_tuple_string(strings_tuple) -> str:
#    return ' '.join(strings_tuple)

# # joining all the tuples
# result = map(join_tuple_string, string_tuples)

# converting and printing the result
# print(list(result))

"""

import numpy as np
import itertools
N,X,K= map(int, input().split())
# X = int(input())
# K = int(input())
S = str(input())
string = S

N,X,K = 10,5,10
S= "1234567891"

s_len = N
box = int(s_len/X)
split_strings = []
n  = X

for index in range(0, s_len, n):
    split_strings.append(string[index : index + n])
ll = [i for i in split_strings]
d = [i for j in ll for i in j]
# print("d: ",d)
new = []

for index in range(0, len(d), n):
    new.append(d[index : index + n])
# print("new: ",new)
out = [x for x in itertools.product(*new)]
# print("out: ",out)
def join_tuple_string(strings_tuple):
   return ''.join(strings_tuple)
final = list(map(join_tuple_string, out))
# print("final: ",final)
for i in range(0, len(final)):
    final[i] = int(final[i])
final.sort()
result = final[K-1]
print(result)
"""












# def listToString(s): 
#     str1 = "," 
#     return (str1.join(s))
# r = listToString(split_strings)
# ll = [i for i in split_strings]

# a = [i for i in ll]