import sys
input = sys.stdin.readline

a=int(input())

lst= list(list(map(int,input().split())) for _ in range(a))
# print(lst)
lst.sort(key=lambda x:x[1])
# print(lst)
lst.sort(key=lambda x:x[0])
# print(lst)
for i in range(a) :
    print(f'{lst[i][0]} {lst[i][1]}')