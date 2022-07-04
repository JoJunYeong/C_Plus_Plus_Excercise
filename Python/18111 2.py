import sys
input = sys.stdin.readline

row, column, inventory = map(int, input().split())
lst=[]
for i in range(row) :
    lst+=list(map(int, input().split()))
set_lst=list(set(lst))
minn=1000000000
result=0
for target in range(min(set_lst), max(set_lst)+1) :
    lst_copy = lst[:]
    time=0
    inventory_tmp = inventory
    for i in lst :
        if i == target :
            continue
        elif i > target :
            time+=2*(i-target)
            inventory_tmp+=(i-target)
        else :
            time+=1*(target-i)
            inventory_tmp-=(target-i)
    if inventory_tmp < 0 :
        time=10000000000
    if time <= minn :
        minn=time
        result = target
    # print(f'time={time}, minn={minn}, target={target}, inventory={inventory_tmp}')
print(f'{minn} {result}')

