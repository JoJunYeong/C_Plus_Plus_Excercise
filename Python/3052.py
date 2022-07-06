from collections import defaultdict

dic=defaultdict()
for i in range(10) :
    a=(int(input())%42)
    if a not in dic :
        dic[a] = 1
    
print(len(dic))