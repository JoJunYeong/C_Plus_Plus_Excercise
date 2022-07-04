a=list(input())
# print(f'a={ord("a")} z={ord("z")} A={ord("A")} Z={ord("Z")}')
for i in range(len(a)) :
    # print(f'a[{i}]={a[i]} ord(a[i])={ord(a[i])}')
    if 97<=ord(a[i])<=122 :
        # 만약 13 더한게 범위를 넘어서면 그걸 보정해줘야 한다.
        if ord(a[i])+13 > 122 :
            a[i]=chr((ord(a[i])+13 )-122+96)
        else :
            a[i]=chr((ord(a[i])+13 ))
    elif 65<=ord(a[i])<=90 :
        if ord(a[i])+13 > 90 :
            a[i]=chr((ord(a[i])+13 )-90+64)
        else :
            a[i]=chr((ord(a[i])+13 ))
    # print(f'a[{i}]={a[i]} ord(a[i])={ord(a[i])}')


    print(a[i],end='')