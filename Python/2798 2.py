from itertools import combinations

a,b = map(int,input().split())

lst= list(map(int,input().split()))

maxx = 0
for i in combinations(lst,3) :
    if maxx<sum(i) <=b :
        maxx=sum(i)
print(maxx)
