array=[0]*42

for i in range(0,10):
    n=int(input())
    array[int(n%42)]+=1

cnt=0
for i in range(0,42):
    if array[i]>0:
        cnt+=1

print(cnt)
