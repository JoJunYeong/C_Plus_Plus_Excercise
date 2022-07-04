from collections import deque
import sys

a,b = map(int, input().split())
sys.setrecursionlimit(100000)

chass_original = list(list( map(str, sys.stdin.readline())) for _ in range(a))
chass_original2=[]
chass_original2 = [item[:] for item in chass_original]
if chass_original2[0][0] == 'W' :
    chass_original2[0][0] = 'B'
else :
    chass_original2[0][0] = 'W'
dx=[1,-1,0,0]
dy=[0,0,1,-1]
mini=100000
chass_copy=[]
chass_copy2=[]

for i in range(a) :
    chass_copy.append([])
    for j in range(b) :
        chass_copy[i].append(0)


for i in range(a) :
    chass_copy2.append([])
    for j in range(b) :
        chass_copy2[i].append(0)

visit=deque()
result=deque()
visit.append([0,0])

# 받아서 쓰는거 말고 맨 처음을 b 이면 w로 바꿔보면 다른결과가 나올수도 있는 가능성을 추가해줘야된다

while visit :
    y,x = visit.popleft()
    result.append([y,x])
    for i in range(4) :
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<b and 0<=yy<a :
            if [yy,xx] in result or [yy,xx] in visit:
                continue
            visit.append([yy,xx])
            if chass_original[yy][xx] == chass_original[y][x] :
                if chass_original[y][x] == 'W' :
                    chass_original[yy][xx] = 'B'
                elif chass_original[y][x] == 'B' :
                    chass_original[yy][xx] = 'W'
                chass_copy[yy][xx]=1

visit2=deque()
result2=deque()
visit2.append([0,0])

while visit2 :
    y,x = visit2.popleft()
    result2.append([y,x])
    for i in range(4) :
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<b and 0<=yy<a :
            if [yy,xx] in result2 or [yy,xx] in visit2:
                continue
            visit2.append([yy,xx])
            if chass_original2[yy][xx] == chass_original2[y][x] :
                if chass_original2[y][x] == 'W' :
                    chass_original2[yy][xx] = 'B'
                elif chass_original2[y][x] == 'B' :
                    chass_original2[yy][xx] = 'W'
                chass_copy2[yy][xx]=1
# print('\n\n')
# print(f'chass_copy')
# print(chass_copy)
# print()
# print(f'chass_copy2')
# print(chass_copy2)
for i in range(a-7) :
    for j in range(b-7) :
        summ=0
        summ2=0
        for ii in range(i,i+8) :
            for jj in range(j,j+8) :
                summ += chass_copy[ii][jj]
                summ2 += chass_copy2[ii][jj]
                if ii==0 and jj==0 :
                    summ2+=1
        mini=min(mini,summ,summ2)
        # print(f'i={i}, j={j}, summ={summ}, summ2={summ2}')









print(mini)

