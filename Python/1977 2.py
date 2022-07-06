lst = list(int(input()) for _ in range(2))
lst2 =[]
for i in range(1,101) :
    lst2.append(i**2)
lst3=[]
for i in lst2 :
    if lst[0] <= i and i <= lst[1]:
        lst3.append(i)
if len(lst3) >=1 :
    print(sum(lst3))
    print(min(lst3))
else : 
    print(-1)




