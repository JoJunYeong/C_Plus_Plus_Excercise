from itertools import combinations, permutations

a= int(input())
lst2 =[]
for i in range(1,a+1) :
    lst2.append(i)
lst=list(permutations(lst2,a))

# print(lst2)
# print(lst)

for i in range(len(lst)) :
    for j in range(a) :
        if j==a-1 :
            print(lst[i][j])
        else :
            print(lst[i][j],'',end='')
