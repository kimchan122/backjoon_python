a=[0]*9
for i in range(0,9):
    n=int(input())
    a[i]=n

max=-1
savei=99

for i in range(0,9):
    if a[i]>=max:
        max=a[i]
        savei=i

print(max)
print(savei+1)
