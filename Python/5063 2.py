a= int(input())
lst = list(list(map(int,input().split())) for _ in range(a))

for i in range(a) :
    if lst[i][1]-lst[i][2] < lst[i][0] :
        print('do not advertise')
    elif lst[i][1]-lst[i][2] > lst[i][0] :
        print('advertise')
    else :
        print('does not matter')