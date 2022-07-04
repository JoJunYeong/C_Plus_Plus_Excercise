a= int(input())
for i in range(a) :
    lst=list(list(map(int,input().split()))for _ in range(9))
    y,k=0,0
    for j in range(9) :
        y+=lst[j][0]
        k+=lst[j][1]
    if y > k :
        print('Yonsei')
    elif y < k :
        print('Korea')
    else :
        print('Draw')

        

