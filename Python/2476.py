a=int(input())
lst = list(list(map(int,input().split())) for _ in range(a))
lst2=[]
for i in range(a) :
    if lst[i][0]==lst[i][1]==lst[i][2] :
        lst2.append(lst[i][0] * 1000 + 10000)
    elif lst[i][0] == lst[i][1] or lst[i][0] == lst[i][2]  :
        lst2.append(lst[i][0] * 100 + 1000)
    elif lst[i][1] == lst[i][2] :
        lst2.append(lst[i][1] * 100 + 1000)
    else :
        lst2.append(max(lst[i][0],lst[i][1],lst[i][2]) * 100)

print(max(lst2))