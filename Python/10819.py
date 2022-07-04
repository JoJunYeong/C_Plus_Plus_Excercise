from itertools import permutations

a=int(input())

lst=list(map(int,input().split()))
maxx=0
for i in permutations(lst,a) :
    total=abs(i[0]-i[1])
    for ii in range(1,a-1) :
        total+=abs(i[ii]-i[ii+1])
    maxx=max(maxx,total)

print(maxx)


