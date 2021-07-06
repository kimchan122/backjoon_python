n=int(input())
min=9999999
max=-9999999
a=[int(j) for j in input().strip().split()]
for i in range(0,n):
    if a[i]<min: min=a[i]
    if a[i]>max: max=a[i]
print(min,max)
