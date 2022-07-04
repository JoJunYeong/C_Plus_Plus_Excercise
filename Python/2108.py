from collections import defaultdict,Counter
import re
import statistics 
import sys
input=sys.stdin.readline

dic = defaultdict()
lst=[]
num=int(input())
for i in range(num):
    try :
        lst.append(int(input()))
    except :
        break
# print('1111111')
print(int(round(sum(lst)/len(lst),0)))   # 1번
lst2 = sorted(lst)
# print('22222222')
print(statistics.median(lst2)) # 2번
# print('22',lst2[(len(lst)//2)-1])    
dic2=Counter(lst)
# print(f'dic2={dic2}')
lst4= sorted(dic2.items() , key= lambda x:x[0])
lst3=dic2.most_common()
lst3.sort(key=lambda x:x[0])
# print(f'lst3={lst3}')
lst3.sort(key=lambda x:x[1], reverse=True)
# print(f'lst3={lst3}')
if len(lst3)>=2 :       # 3번
    if lst3[0][1] == lst3[1][1] :
        # print('3333333333')
        print(lst3[1][0])
    else :
        # print('3333333333')
        print(lst3[0][0])
else :
    # print('3333333333')
    print(lst3[0][0])
# print('44444444')
print(lst2[-1]-lst2[0]) # 4번

