n,x=map(int,input().split())
a=[int(k) for k in input().strip().split()]
for i in range(0,n):
    if(a[i]<x): print(str(a[i])+" ",end='')
