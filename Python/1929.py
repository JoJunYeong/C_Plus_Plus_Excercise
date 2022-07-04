import sys
input = sys.stdin.readline

a,b=map(int,input().split())
lst=[True]*(b+1)
m=int(b**0.5)
for i in range(2,m+1) :
    
    if lst[i] == True :
        for j in range(i+i,b+1,i):
            lst[j]= False
    # print(f'i={i}, lst={lst}')
lst=list(i for i in range(2,b+1) if lst[i] == True )
for i in range(len(lst)):
    if lst[i] >= a :
        print(lst[i])
