a = int(input())
lst=list(list(map(int,input().split())) for _ in range(a))
q1,q2,q3,q4,axis=0,0,0,0,0

for i in range(a) :
    if lst[i][0] == 0 or lst[i][1]==0 :
        axis+=1
    elif lst[i][0]>0 and lst[i][1]>0 :
        q1+=1
    elif lst[i][0]<0 and lst[i][1]>0 :
        q2+=1
    elif lst[i][0]<0 and lst[i][1]<0 :
        q3+=1
    else:
        q4+=1

print('Q1:',q1)
print('Q2:',q2)
print('Q3:',q3)
print('Q4:',q4)
print('AXIS:',axis)
