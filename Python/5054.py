num= int(input())

for _ in range(num) :
    a= int(input())
    lst=list(map(int,input().split()))
    print((max(lst)-min(lst))*2)
    

