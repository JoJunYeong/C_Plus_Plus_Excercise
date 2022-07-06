import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

a,b=map(int, input().split())
lst = list(map(int,list(input() for _ in range(a))))
first,last=1,max(lst)

while first <= last :
    middle = (first+last)//2
    summ=0
    for i in range(a) :
        summ+=(lst[i]//middle)
    if summ >= b :
        # print(f'middle={middle} first={first} last={last}')
        # return binary_search(key, middle+1, last, list)
        first=middle+1
    else :
        # return binary_search(key, first, middle-1, list)
        last=middle-1
    print(f'middle={middle}, first={first}, last={last}')
print( last )








