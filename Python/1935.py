count = int(input())
lst = list(input())
lst2 = list(input() for _ in range(count))
count2=0
while True :
    # print('count2=',count2)
    if count2 >= len(lst) :
        break
    
    for j in range(65,65+len(lst2)) :
        # print(lst)
        # print('lst[count]=',lst[count2])
        # print('ord(lst[count])=',ord(lst[count2]))
        if ord(lst[count2]) == j :
            # print('entrance ord(lst[i])=',ord(lst[count2]))
            lst[count2] = float(lst2[j-65])
            break
            
    
    if lst[count2] == '*' :
        lst[count2-2] = float(lst[count2-2])*float(lst[count2-1])
        lst.remove(lst[count2-1]) 
        lst.remove(lst[count2-1])
        count2-=2
    elif lst[count2] == '+' :
        lst[count2-2] = float(lst[count2-2])+float(lst[count2-1])
        lst.remove(lst[count2-1]) 
        lst.remove(lst[count2-1])
        count2-=2
    elif lst[count2] == '/' :
        lst[count2-2] = float(lst[count2-2])/float(lst[count2-1])
        lst.remove(lst[count2-1]) 
        lst.remove(lst[count2-1])
        count2-=2
    elif lst[count2] == '-' :
        lst[count2-2] = float(lst[count2-2])-float(lst[count2-1])
        lst.remove(lst[count2-1]) 
        lst.remove(lst[count2-1])
        count2-=2
    count2+=1

print( '{:.2f}'.format(lst[0]) )



