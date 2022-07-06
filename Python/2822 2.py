from collections import defaultdict

dic=defaultdict()
for i in range(1,9) :
    dic[i]=int(input())
dic = sorted(dic.items() , key=lambda x:x[1])
sumi=0
lst=[]
for i in range(3,8) :
    a,b=dic[i]
    lst.append(a)
    sumi+=b
print(sumi)
lst.sort()
print(f'{lst[0]} {lst[1]} {lst[2]} {lst[3]} {lst[4]}')