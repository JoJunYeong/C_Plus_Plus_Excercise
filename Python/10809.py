from collections import defaultdict
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lst=list(input())
dic=defaultdict()
for i in range(len(lst)) :
    if lst[i] not in dic :
        dic[lst[i]] = i
for i in range(len(alphabet)) :
    if alphabet[i] in dic :
        print(dic[alphabet[i]],'',end='')
    else :
        print(-1,'',end='')
