lst=list(list(map(int,input().split())) for _ in range(10))
sum=0
lst2=[]
for i in range(10) :
    sum = sum+lst[i][1]-lst[i][0]
    lst2.append(sum)
print(max(lst2))