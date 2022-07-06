from itertools import combinations, combinations_with_replacement,permutations
from collections import defaultdict

def solution(n, info):
    answer=[0]*11
    number=[0,1,2,3,4,5,6,7,8,9,10]
    combi = combinations_with_replacement(number,n)
    dic=defaultdict()
    lst=[]
    for i in combi :
        b=0
        for j in range(1,12) :
            a=[]
            a.append([i])
            # print(f'a[0][0].count({j})={a[0][0].count(j)} , info[10-{j}]+1={info[10-j]+1} ,   a={a}')
            if a[0][0].count(j) > info[11-j]+1 :
                b=1
                break
            if a[0][0].count(j) < info[11-j]+1 and  a[0][0].count(j) !=0 :
                b=1
                break
        if b==0 :
            lst.append([i])
    lst = sorted(lst, key=lambda x:x[0], reverse=True)

    maxi=0
    for i in lst :

        sumi=0
        lst2=[0]*11
        for j in range(0,11) :
            if i[0].count(j) > info[10-j] :
                sumi+=j
                lst2[10-j]=i[0].count(j)
        if lst2[7]==1 :
            print(f'lst2={lst2}')
        if sumi>= maxi :
            maxi=sumi
            for qq in range(11) :
                answer[qq]=lst2[qq]

            print(f'msxi={maxi}, sumi={sumi}')
            print(f'answe={answer}')
            print(f'lst2={lst2}\n')
            
            
    print(answer)


    return answer


solution(10, [0,0,0,0,0,0,0,0,3,4,3])

