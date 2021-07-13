array=[0]*10002
def solve(a):
    res=0
    res+=a
    while a>0:
        if a==0:
            break
        else:
            res+=int(a%10)
            a/=10
    if(res<=10000):
        array[res]=1
for i in range(1,10001):
    solve(i)
for i in range(1,10001):
    if array[i]==0:
        print(i)