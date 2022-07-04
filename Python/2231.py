import sys
sys.setrecursionlimit(1000000)

target=list(input())
a=''
for i in range(len(target)):
    a+=target[i]
a=int(a)

for i in range(0,a) :
    result=i
    result_str=list(str(result))
    for j in result_str :
        result+=int(j)
    if result==a :
        print(i)
        break
    if i==a-1 :
        print(0)

