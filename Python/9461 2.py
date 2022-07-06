import sys

input=sys.stdin.readline
itera = int(input())

for _ in range(itera) :
    number=int(input())
    number_lst=[]
    number_lst.append(1)
    number_lst.append(1)
    number_lst.append(1)

    if number==1 :
        print(1)
    elif number==1 :
        print(1)
    elif number==2 :
        print(1)

    else :
        for i in range(3,number) :
            number_lst.append(number_lst[i-2]+number_lst[i-3])
            # print(f'i={i}, number_lst[{i-2}]={number_lst[i-2]}, number_lst[{i-3}]={number_lst[i-3]}')
            # print(f'number_lst={number_lst}\n')
        print(number_lst[-1])


