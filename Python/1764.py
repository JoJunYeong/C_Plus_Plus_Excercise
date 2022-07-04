
a,b = map(int,input().split())

set_a = set()
for i in range(a) :
    set_a.add(input())

set_b = set()
for i in range(b) :
    set_b.add(input())

result = sorted(list(set_a & set_b))
aa=len(result)
print(aa)
for i in range(aa) :
    print(result[i])





















# from collections import defaultdict

# dic = defaultdict()
# lst=[]
# a,b = map(int, input().split())

# for i in range(a) :
#     dic[input()]=1
    
# for i in range(b) :
#     name = input()
#     if name not in dic :
#         continue
#     else :
#         lst.append(name)

# lenn=len(lst)
# print(lenn)
# lst.sort()
# for i in range(lenn) :
#     print(lst[i])

