import sys
input= sys.stdin.readline

a=int(input())
lst = list(list(map(int,input().split())) for _ in range(a))

lst.sort(key=lambda x:(x[1],x[0]))

for i in range(a) :
    print(lst[i][0],lst[i][1])


