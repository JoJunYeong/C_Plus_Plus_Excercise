from collections import deque



while True :
    try :
        a=input()
    except EOFError:
        break
    # print(a)
    if a=='.' :
        break
    dq=deque()

    for i in range(len(a)) :
        
        if a[i] == '(' :
            dq.append('(')
        elif a[i] == '[' :
            dq.append('[')
        elif a[i] == ')' :
            if len(dq) == 0:
                print('no')
                break
            if  dq[-1]== '(' :
                dq.pop()
            else :
                print('no')
                break
                
        elif a[i] == ']' :
            if len(dq) == 0:
                print('no')
                break
            if dq[-1] ==  '[' :
                dq.pop()
            else :
                print('no')
                break
                
        if a[i] == '.' or i==len(a)-1:
            if len(dq) == 0 :
                print('yes')
                break
            else :
                print('no')
                break
        # print(f'dq={dq}, a[{i}]={a[i]}')