from collections import defaultdict
import operator

a= int(input())
lst = list(input() for _ in range(a))

for i in range(a) :
    dic = defaultdict()
    for j in range(len(lst[i])) :
        s=lst[i][j:j+1]
        if s in dic :
            if lst[i][j:j+1] != lst[i][j-1:j] :
                dic[s]=2
            continue
        else :
            dic[s] = 1
    sort = sorted(dic.items(), key=operator.itemgetter(1))
    if sort[len(sort)-1][1] == 2 :
        a-=1
print(a)