from collections import defaultdict
import sys
input=sys.stdin.readline

dic = defaultdict()

many, questions = map(int, input().split())
for i in range(1,many+1) :
    tmp = input()
    tmp= tmp.rstrip('\n')
    dic[i] = tmp
lst2=list(dic.values())
# print(f'lst2={lst2}')
# print(f'dic={dic}')

for i in range(questions) :
    tmp=input()
    tmp=tmp.rstrip('\n')
    if tmp.isdigit() :
        print(dic[int(tmp)])
    else :
        print(lst2.index(tmp)+1)
        









