n=int(input())
array=[int(i) for i in input().strip().split()]
max=-1
avg=0

for i in range(0,n):
    if max<array[i]:
        max=array[i]

array2=[0]*n
for i in range(0,n):
    array2[i]=array[i]/max*100
    avg=avg+array2[i]

avg=avg/n
print(avg)
