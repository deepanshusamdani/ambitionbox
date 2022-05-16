import math
def strRating(strin):
    str1 = float(strin)
    l = []
    f,i = math.modf(str1)
    i = int(i)
    flot = round(f,2)
    c = "full"
    h = "half"
    n = "empty"
    for x in range(i+1):
        if i>x:
            l.append(c)
        else:
            l.append(h)
    ll = len(l)
    tot = 5-ll
    for i in range(tot):
        l.append(n)
    for i in out:
        print(i,end =' ')

out = strRating('2.36')


