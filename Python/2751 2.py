import sys
input=sys.stdin.readline

a=int(input())
lst=list(int(input()) for _ in range(a))
lst.sort()
# print(lst)
            
for i in range(a) :
    print(lst[i])