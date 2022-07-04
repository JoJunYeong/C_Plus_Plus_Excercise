
a= int(input())
lst = list(input() for _ in range(a))
lst = list(set(lst))
lst.sort()
lst.sort(key = len)
for i in lst :
    print(i)


