def rotateWord(str,k):
    strRotate = str.split()
    for i in range(0,k):
        print("i: ",i)
        for j in range(0, len(strRotate)):
            print("j: ",j)
            strRotate[j] = strRotate[j][1:] + strRotate[j][0]
            print("s: ",strRotate[j])
    count = 0
    for k in range(0, len(strRotate)):
        if strRotate[k] in str:
            count+=1
    print(count)
#calling rotateword function
rotateWord("adaada", 3)