a=int(input())
lst = list(list(map(int,input().split())) for _ in range(a))
sum=0
for i in range(a) :
    sum+=lst[i][1]%lst[i][0] 
print(sum)