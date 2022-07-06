a=int(input())

for i in range(a) :
    lst=list(map(int,list(input().split())))
    lst.sort()
    del lst[0]
    del lst[-1]
    if max(lst)-min(lst) >= 4 :
        print('KIN')
    else :
        print(sum(lst))


