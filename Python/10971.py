a= int(input())

lst = list(input().split() for _ in range(a))

for i in range(a) :
    for j in range(a) :
        if int(lst[i][j]) == 0 :
            lst[i][j] = 100000000
        else :
            lst[i][j] = int(lst[i][j])

print(lst)

q,w=0,0
sum=0
for i in range(a) :
    sum+=min(lst[q])
    q=lst[q].index(min(lst[q]))
    for j in range(a) :
        lst[j][q] = 100000000


print(lst)
print(sum)


