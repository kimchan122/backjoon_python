n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    c=int(a+b)
    d="Case #"+str(i)+": "+str(a)+" + "+str(b)+" = "+str(c)
    print(d)
