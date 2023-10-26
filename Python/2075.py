import sys

input = sys.stdin.readline
hq = []
over =False
n = int(input())
for _ in range(n) :
    for a in list(map(int,input().split())) :
        if over :
            if a > hq[-1] :
                hq.append(a)
                hq.sort(reverse=True)
                hq.pop()
            continue
        if len(hq) > n :
            over = True
        hq.append(a)
        hq.sort(reverse=True)

print(hq[n-1])


