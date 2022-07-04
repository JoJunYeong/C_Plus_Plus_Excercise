a= int(input())
lst= list( list(map(int,input().split())) for _ in range(a))

for i in range(a) :
    print(lst[i][0]+lst[i][1])


