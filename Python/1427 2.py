lst=list(map(int,list(input())))
lst = sorted(lst, reverse=True)

for i in range(len(lst)) :
    print(lst[i],end='')

