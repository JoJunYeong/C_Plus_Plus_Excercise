import sys
input=sys.stdin.readline

a= int(input())
d=[0]*(a+1)
d[0],d[1] = 0,1

for i in range(2,a+1) :
    minn = 1e9
    j=1
    while j**2 <= i :
        
        minn=min(minn,d[i-(j**2)])
        d[i] = minn+1
        j+=1
print(d[a])





