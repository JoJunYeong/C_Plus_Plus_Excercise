iteration = int(input())
lst = list(list(input()) for _ in range(iteration))

for i in range(iteration) :
    lst[i].remove(" ")


for i in range(iteration) :
    lst[i][0]=int(lst[i][0])
    for j in range(1,len(lst[i])) :
        print(lst[i][j]*lst[i][0],end='')
    print()


