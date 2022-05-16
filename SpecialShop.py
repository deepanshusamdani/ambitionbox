"""
https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/special-shop-69904c91/
"""

def calc():
    x=(n*b)//(a+b)
    y=n-x
    if(abs(x*(a+b)-(n*b))>abs((x+1)*(a+b)-(n*b))):
        x=x+1
        y=n-x
    return a*(x**2)+b*(y**2)

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        par=list(map(int,input().split()))
        n,a,b=par[0:3]
        print(calc())