"""
    Minimum Jumps
    Bob lives with his wife in a city named Berland. Bob is a good husband, 
    so he goes out with his wife every Friday to Arcade mall.
    Arcade is a very famous mall in Berland. It has a very unique transportation 
    method between shops. Since the shops in the mall are laying in a straight line, 
    you can jump on a very advanced trampoline from the shop i, 
    and land in any shop between (i) to (i+Arr[i]), where Arr[i] is a constant given for each shop.
    There are N shops in the mall, numbered from 0 to N-1. 
    Bob's wife starts her shopping journey from shop 0 and ends it in shop N-1.
    As the mall is very crowded on Fridays, unfortunately, Bob gets lost from his wife. 
    So he wants to know, what is the minimum number of trampoline jumps from shop 0 he has 
    to make in order to reach shop N-1 and see his wife again. If it is impossible to reach the last shop, return -1.


    1 <= T <= 10
    1 <= N <= 5 * 10^4
    0 <= Arr[i] <= N
    Where T is the number of test cases, 
    N is the size of the array 
    and Arr[i] is the ith element in the array.
"""

def minimumJumps(arr, n):
    if (n == 1):
        return 0
    if (arr[0] == 0):
        # we cannot jump from this shop
        return -1
    jumpsTaken = 1
    maxReach = arr[0]
    stepsLeft = arr[0]
    for i in range(1, n - 1):
        maxReach = max(maxReach, i + arr[i])
        # we took a step to reach current index
        stepsLeft -= 1
        if (stepsLeft == 0):
            jumpsTaken += 1
            if (i >= maxReach):
                # Impossible to reach the last shop
                return -1
            stepsLeft = maxReach - i
    return jumpsTaken