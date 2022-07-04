import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000000)


many, target = map(int, input().split())
lst=list(map(int, input().split()))

start,last = 0,max(lst)
while start<= last :
    middle = (start+last)//2
    summ=0

    for i in lst :
        if i >= middle :
            summ+= i-middle
    
    if summ >= target :
        start = middle+1
    else :
        last = middle-1

print(last)


