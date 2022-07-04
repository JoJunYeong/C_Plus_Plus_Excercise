from itertools import permutations

lst=list(int(input()) for _ in range(9))
permu=permutations(lst,7)
for i in permu :
    if sum(i) == 100 :
        i = sorted(i, reverse=False)
        for j in range(7) :
            print(i[j])
        break
