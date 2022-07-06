lst = list(input() for _ in range(3))


if lst[1]=='*' :
    print(int(lst[0])*int(lst[2]))    
elif lst[1]=='+' :
    print(int(lst[0])+int(lst[2]))   