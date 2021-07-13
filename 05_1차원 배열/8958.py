n=int(input())
for i in range(0,n):
    cnt=0
    res=0
    str=input()
    for j in range(0,len(str)):
        if str[j]=='O':
            cnt=cnt+1
            res+=cnt
        elif str[j]=='X':
            cnt=0
    print(res)
