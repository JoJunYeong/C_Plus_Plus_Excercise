a=int(input())

for k in range(a) :
    lst=list(map(int,input().split()))
    b=lst[0]
    del lst[0]
    lst.sort()
    minn=101
    maxx=0
    gap=0
    for i in range(len(lst)) :
        if i!=0 and gap<(lst[i]-lst[i-1]):
            gap=lst[i]-lst[i-1]
        if lst[i] > maxx :
            maxx=lst[i]
        if lst[i] < minn :
            minn=lst[i]
    print(f'Class {k+1}')
    print(f'Max {maxx}, Min {minn}, Largest gap {gap}')