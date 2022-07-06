a = int(input())

for i in range(a) :
    num = int(input())
    lst = list(input().split() for _ in range(num))
    lst2=[]
    for i in range(num) :
        lst2.append(int(lst[i][1]))
    print(lst[lst2.index(max(lst2))][0])

