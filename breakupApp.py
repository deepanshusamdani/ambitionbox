"""
https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/breakup-app/
"""

t = int(input())
g = []
m = []
for i in range(t):
    a = input()
    b = [int(i) for i in a.split() if i.isdigit()]
    if a[0] =='G':
        for i in range(len(b)):
            g.append(b[i])
    else:
        for i in range(len(b)):
            m.append(b[i])
count_19 = 0
count_20 = 0
count_not = 0
for i in range(len(g)):
    if g[i] ==19:
        count_19 +=2
    elif g[i] ==20:
        count_20 +=2
    else:
        count_not +=2
for j in range(len(m)):
    if m[j] ==19:
        count_19 +=1
    elif m[j] ==20:
        count_20 +=1
    else:
        count_not +=1

if count_19 >0:
    if count_19 <= count_not:
        print('No Date')
    else:
        print('Date')
else:
    if count_20 <= count_not:
        print('No Date')
    else:
        print('Date')