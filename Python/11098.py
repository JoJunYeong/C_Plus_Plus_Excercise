a= int(input())

for i in range(a) :
    num = int(input())
    lst=list(input().split() for _ in range(num)) 
    lst2=[]
    for j in range(num) :
        lst2.append(int(lst[j][0]))
    print(lst[lst2.index(max(lst2))][1])    




