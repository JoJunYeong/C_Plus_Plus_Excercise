a=int(input())

for _ in range(a) :
    summ=0
    minn=1000
    lst = list(map(int,input().split()))
    for i in range(len(lst)) :
        if lst[i] % 2 ==0 :
            summ+=lst[i]
            if lst[i] < minn :
                minn=lst[i]
    print(f'{summ} {minn}')





