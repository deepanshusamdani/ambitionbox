"""
    Minimum Cost To Connect Sticks
    You are given an array/list ARR of N positive integers where each element 
    describes the length of the stick. You have to connect all sticks into one. 
    At a time, you can join any two sticks by paying a cost of X and Y
    where X is the length of the first stick and Y is the length of the second 
    stick and the new stick we get will have a length equal to (X+Y). 
    You have to find the minimum cost to connect all the sticks into one.


    1 <= T <= 10
    1 <= N <= 10^4
    1 <= Val <= 5*10^3
    Where T represents the number of test cases, 
    N represents the number of sticks, 
    and Val represents the initial length of any stick.

"""

from heapq import heappush, heappop

def minimumCostToConnectSticks(arr):

    # Creating a min-heap.
    minHeap = []
    print("arr-len: ",len(arr))
    # Pushing all the elements into the min-heap
    for i in range(len(arr)):
        heappush(minHeap, arr[i])
    print("minHeap : ",minHeap)
    # Create a minCost variable to store the answer.
    minCost = 0
    '''
        While the size of the min-heap is greater than 1.
        Pop out first two minimum elements.
        Add it to the minCost.
        Also add the new length of stick into the min-heap.
    '''
    while (len(minHeap) > 1):

        firstMinimum = heappop(minHeap)
        secondMinimum = heappop(minHeap)
        print("fMin: ",firstMinimum)
        print("sMin: ",secondMinimum)
        minCost += firstMinimum + secondMinimum
        print("minCost: ",minCost)
        heappush(minHeap, firstMinimum + secondMinimum)
    print("minHeap2: ", minHeap)
    return minCost
# [1,2,3,4,5,6,7,8]
out = minimumCostToConnectSticks([3,2,1,4,5])
print("out: ",out)