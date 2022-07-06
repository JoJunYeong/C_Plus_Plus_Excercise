a=int(input())
lst=list(input().split() for _ in range(a))
lst2=[]
for i in range(a) :
    lst2.append((31-int(lst[i][1]))+((12-int(lst[i][2]))*30)+int((2500-int(lst[i][3]))*365))
print(lst[lst2.index(min(lst2))][0])
print(lst[lst2.index(max(lst2))][0])
