h,m=map(int,input().split())
m-=45
if m<0: m,h=m+60,h-1
if h<0: h=h+24
print(h,m)
