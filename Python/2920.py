lst=list(map(int,input().split()))
# print(lst)
if lst[0]==1 :
    for i in range(1,8) :
        if lst[i]!=lst[i-1]+1 :
            print('mixed')
            break
        if i==7 :
            print('ascending')
elif lst[0]==8 :
    for i in range(1,8) :
        if lst[i]!=lst[i-1]-1 :
            print('mixed')
            break
        if i==7 :
            print('descending')

else :
    print('mixed')

