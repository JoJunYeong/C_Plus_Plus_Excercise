a=int(input())
lst = list(map(int,input().split()))
b=0
for i in range(len(lst)) :
    if lst[i]==a :
         b+=1

print(b)