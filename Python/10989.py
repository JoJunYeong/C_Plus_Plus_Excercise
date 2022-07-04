import sys
input = sys.stdin.readline

a=int(input())
lst=[0]*10001
for i in range(a) :
    lst[int(input())]+=1

for i in range(10001) :
    for j in range(lst[i]) :
        print(i)

