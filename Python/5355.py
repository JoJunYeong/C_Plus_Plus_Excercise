a = input()
lst = list(input().split() for _ in range(int(a)))

for i in range(int(a)) :
    for j in range(len(lst[i])) :
        lst[i][0] = float( lst[i][0] )
        if lst[i][j] == '@' :
            lst[i][0] = lst[i][0] * 3
        elif lst[i][j]=='%' :
            lst[i][0] = lst[i][0] + 5
        elif lst[i][j]=='#' : 
            lst[i][0] = lst[i][0] - 7
    print('%.2f' %lst[i][0])


