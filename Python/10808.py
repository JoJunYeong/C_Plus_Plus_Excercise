from collections import defaultdict 

dic = defaultdict()
a= list(input())
for i in a :
    if i not in dic :
        dic[i]=1
    elif i in dic :
        dic[i]+=1
for i in range(97,123) :
    if chr(i) in dic :
        print(dic[chr(i)],'',end='')
    else :
        print(0,'',end='')


