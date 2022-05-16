input = [1,2,3,5,8]
for i in input:
    # print(i)
    input.sort()
    if (input[i+1] - input[i]) > 1:
        a = input[i+1]
        b = input[i]
        c = b+1
        print("c: ",c)
        input.append(c)
        print(input)
    else:
        print("no missing element",i,i+1)


def getMissingNo(a, n):
    i, total = 0, 1
    print("i: ",i)
    for i in range(2, n + 2):
        print("inside: ",i)
        total += i
        print("total: ",total)
        total -= a[i - 2]
        print("total2: ",total)
    return total
