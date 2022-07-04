a= int(input())

for i in range(a) :
    lst=list(map(int, list(input().split())))
    lst=sorted(lst,reverse=True)
    print(lst[2])






