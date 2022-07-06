
a=int(input())


for i in range(a) :
    b = int(input())
    lst = []
    
    lst.append(1)
    lst.append(2)
    lst.append(4)
    for j in range(3,b) :
        lst.append(lst[j-1]+lst[j-2]+lst[j-3])
    if b==1 :
        print(lst[0])
    elif b==2 :
        print(lst[1])
    elif b==3 :
        print(lst[2])
    else :
        print(lst[-1])