lst=list(list(map(int,input().split())) for _ in range(4))

lst2=[]
sum=0
for i in range(4) :
    sum=sum-lst[i][0]+lst[i][1]
    lst2.append(sum)
print(max(lst2))