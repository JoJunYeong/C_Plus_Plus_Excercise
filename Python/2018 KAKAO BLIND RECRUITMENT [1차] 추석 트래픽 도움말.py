lines=[
"2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"
]
from decimal import Decimal

lst2=[]
for i in range(len(lines)) :
        lst2.append([])
        lst=lines[i].split()
        lst_split = list(map(float,lst[1].split(':')))
        a,b=lst[2].split('s')
        a=float(a)
        # print(f'a={a}')
        lst2[i].append(float((Decimal(lst_split[0]*3600)+Decimal(lst_split[1]*60)+Decimal(lst_split[2]))-(Decimal(a)-Decimal(0.001))))
        lst2[i].append(((lst_split[0]*3600)+(lst_split[1]*60)+lst_split[2]))
print(lst2)
maxi=0

for i in range(len(lst2)):
    for j in range(2) :
        a= lst2[i][j]   # 1초 시간막대의 시작점
        b=round(float(Decimal(a+1)-Decimal(0.001)),3)   # 1초 시간막대의 끝점
        cnt=0
        for k in range(len(lst2)) :
            if (a<=lst2[k][0]<=b ) or (a<=lst2[k][1]<=b) or (lst2[k][0]<=a and b<=lst2[k][1]) :
                cnt+=1
        maxi = max(cnt,maxi)

print(max)
