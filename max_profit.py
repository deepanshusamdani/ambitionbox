import itertools

def maxprofit(j):
    res = [] 
    jj = list(itertools.combinations(j,2))
    for i in range(len(jj)):
        res.append(jj[i][1]-jj[i][0])
    max_res = max(res)
    if max_res > 0:
        return max_res
    else:
        return 0

if __name__ == "__main__":
    input = [7,8,9,2,5,13,0]
    # [7,1,5,3,6,4] # [7,6,4,3,1]
    output = maxprofit(input)
    print(output)