from collections import defaultdict
lst = list(map(int,list(input() for _ in range(10))))
print(int(sum(lst)/10))

dic=defaultdict()

for i in range(len(lst)) :
    if lst[i] not in dic :
        dic[lst[i]] = 1
    else :
        dic[lst[i]] += 1

lst2=sorted(dic.items(),key = lambda x:x[1],reverse=True)
print(lst2[0][0])
