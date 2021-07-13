array=[0]*10

a=int(input())
b=int(input())
c=int(input())

x=a*b*c

while x>=0:
    if x==0:
        break
    else:
        k=int(x%10)
        array[k]+=1
        x=int(x/10)

for i in range(0,10):
    print(array[i])
