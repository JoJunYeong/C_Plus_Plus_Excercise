a= int(input())

for _ in range(a) :
    aa,bb = map(int, input().split())
    lst=[]
    for i in range(aa) :
        aaa=int(input())
        if aaa not in lst :
            lst.append(aaa)
    print(f'{aa-len(lst)}')



