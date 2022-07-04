a = int(input())
pibo_lst = []

for i in range(a+1) :
    if i == 0 or i == 1:
        pibo_lst.append(i)
    else :
        pibo_lst.append(pibo_lst[-1]+pibo_lst[-2])
print(pibo_lst[-1])