from collections import deque
import sys
input=sys.stdin.readline
a,b = map(int,input().split())

map_original = list(list(map(int,input().split())) for _ in range(b))
coordinate_dq=deque()
total_cnt = a*b     # 토마토의 총 개수
tmp_cnt=1
dx=[1,-1,0,0]
dy=[0,0,1,-1]

for i in range(b) : # map을 한번 싹 훑는 작업 이때 total count도 정확하게 끝내고 좌표를 이용해서 그래프관계도도 그려놓아야 된다.
    for j in range(a) :
        tmp_cnt+=1
        if map_original[i][j] == -1 :
            total_cnt-=1
        if map_original[i][j] == 1 :
            coordinate_dq.append([i,j,0])
            total_cnt-=1

# print(total_cnt)
# print(coordinate_dq)
cnt=0
result=deque()

if len(coordinate_dq) == 0 :
    print(-1)
else :
    y,x,day = coordinate_dq.popleft()

    while True :
        for i in range(4) :
            ddy=dy[i]+y
            ddx=dx[i]+x
            if ddx < 0 or ddx >= a or ddy < 0 or ddy >= b :
                continue
            if map_original[ddy][ddx] != -1 and map_original[ddy][ddx] != 1 :
                coordinate_dq.append([ddy,ddx,day+1])
                map_original[ddy][ddx]=1
                total_cnt-=1
        # print(f'coordinate_dq={coordinate_dq}')
        cnt+=1
        if len(coordinate_dq) == 0 :
            break
        y,x,day = coordinate_dq.popleft()
        # print(f'total_cnt={total_cnt}')
        

    if total_cnt == 0:
        print(day)
    else :
        print(-1)
