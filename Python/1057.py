
import sys

input = sys.stdin.readline


cantidate,jimin,hansu = map(int, input().split())


floor =0
summ=0
jimin_index,hansu_index=0,0
for i in range(1,cantidate) :
    
    summ+=2**i
    if 2**(i-1) <= cantidate <= 2**i :
        floor=i
        jimin = summ-2**i+jimin
        hansu = summ-2**i+hansu
        break
# print(f'floor = {floor}, summ={summ}, jimin_index={jimin_index}, hansu_index={hansu_index}')
lst=list(i for i in range(1,summ+1))

# print(lst)
roundd=0
while True :
    roundd+=1
    if jimin%2==0 :
        parent_jimin = (jimin-2)//2
    elif jimin%2==1 :
        parent_jimin = (jimin-1)//2

    if hansu%2==0 :
        parent_hansu = (hansu-2)//2
    elif hansu%2==1 :
        parent_hansu = (hansu-1)//2

    if parent_jimin == parent_hansu : 
        print(roundd)
        break
    if parent_jimin == 0 or parent_hansu == 0 :
        print(-1)
        break
    jimin = parent_jimin
    hansu = parent_hansu




