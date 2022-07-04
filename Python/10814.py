
a=int(input())
lst=[]
for i in range(a) :
    a,b = input().split()
    a=int(a)
    lst.append([])
    lst[i].append(a)
    lst[i].append(b)
lst.sort(key=lambda x:x[0])
for i in range(len(lst)) :
    print(f'{lst[i][0]} {lst[i][1]}')
