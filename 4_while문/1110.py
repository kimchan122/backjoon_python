n=int(input())
k=n
cnt=0
while True:
    a=int(k/10)
    b=int(k%10)
    k=int(b*10+(a+b)%10)
    cnt+=1
    if k==n:
        break
print(cnt)
