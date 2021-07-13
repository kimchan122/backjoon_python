n=int(input())
for i in range(0,n):
    a=[int(i) for i in input().strip().split()]
    avg=0
    cnt=0
    for j in range(1,a[0]+1):
        avg+=a[j]
    avg/=a[0]
    #print("AVG: ",avg)
    for j in range(1,a[0]+1):
        if avg<a[j]:
            cnt+=1
    #print("CNT: ",cnt)
    res="{:.3f}%".format(round(cnt/a[0]*100,3))
    print(res)
