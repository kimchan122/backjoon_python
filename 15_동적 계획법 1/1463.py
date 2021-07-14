n=int(input())
array=[-1 for i in range(50)]

for i in range(0,n):
    zero=0
    one=0
    k=int(input())
    fib(k)
    print(zero, one)


def fib(num):
    array[0]=1
    array[1]=1

    if num==0:
        zero+=1
        return 1
    elif num==1:
        one+=1
        return 1
    else:
        if array[num]!=-1:
            return array[num]
        else:
            return fib(num-1)+fib(num-2)
