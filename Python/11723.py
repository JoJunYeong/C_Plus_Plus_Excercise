import sys

input= sys.stdin.readline

a=int(input())
number_lst= 0b00000000000000000000

for i in range(a) :
    string = input()
    if string[0:2] == 'ad':
        order, number = string.split()
        number_lst=number_lst | (1<<21-int(number))
            
    elif string[0:1] == 'r':
        order, number = string.split()
        number_lst=number_lst & ~(1<<21-int(number))
    
    elif string[0:1] == 'c':
        order, number = string.split()
        if number_lst & (1<<21-int(number)) != 0b000000000000000000000:
            print(1)
        else :
            print(0)
    
    elif string[0:1] == 't':
        order, number = string.split()
        if number_lst & (1<<21-int(number)) != 0b000000000000000000000:
            number_lst=number_lst & ~(1<<21-int(number))
        else :
            number_lst=number_lst | (1<<21-int(number))
    
    elif string[0:2] == 'al':
        number_lst= 0b11111111111111111111
    
    elif string[0:1] == 'e':
        number_lst= 0b00000000000000000000
    # print(Af'\nstring = {string}, number_lst={bin(number_lst)}\n')




