from itertools import permutations

lst=list(map(int,list(input() for _ in range(9))))

combi=permutations(lst,7)

for i in combi :
    if sum(i) == 100 :
        i=sorted(i,reverse=False)
        for j in range(7) :
            print(i[j])
        break




