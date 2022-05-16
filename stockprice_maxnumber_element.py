import itertools
def stock(j):
    res = [] 
    jj = list(itertools.combinations(j,2))
    print("jj: ",jj)
    for i in range(len(jj)):
        res.append(jj[i][1]-jj[i][0])
    print("res: ",res)
    max_res = max(res)
    print("max_res: ",max_res)
    ind = res.index(max_res)
    print("ind: ",ind)
    new = jj[ind][0]
    return new

input = [5,10,12,4,5,9]
output = stock(input)
print(output)

# print max profit by element