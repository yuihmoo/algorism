a,b=map(int,input().split())
c=int(input())
d=b+c
e=d//60
if e>=1 and 0<=c<=1000:
    a=a+e
    d=(b+c)%60
    if a==24:
        a=0
        d=(b+c)-60
print("%d %d"%(a,d))