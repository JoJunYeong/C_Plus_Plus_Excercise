import sys

input = sys.stdin.readline

n,m = map(int,input().split())
r,c,d = map(int,input().split())
lst = list(list(map(int, input().split())) for _ in range(n))

dx=[-1,0,1,0]   # 동서남북에 맞춰서 좌표상 왼쪽을 검사할 수 있도록 해놓음
dy=[0,-1,0,1]   # 동서남북에 맞춰서 좌표상 왼쪽을 검사할 수 있도록 해놓음
back_dx=[0,-1,0,1]
back_dy=[1,0,-1,0]
i=0
cnt=1
lst[r][c]=2
while i<4 : 
    
    i+=1
    if (lst[r+dy[0]][c+dx[0]] == 1 or lst[r+dy[0]][c+dx[0]] == 2) and (lst[r+dy[1]][c+dx[1]] == 1 or lst[r+dy[1]][c+dx[1]] == 2) and (lst[r+dy[2]][c+dx[2]] == 1 or lst[r+dy[2]][c+dx[2]] == 2) and (lst[r+dy[3]][c+dx[3]] == 1 or lst[r+dy[3]][c+dx[3]] == 2) and  lst[r+back_dy[d]][c+back_dx[d]] != 1 :
        r,c=r+back_dy[d],c+back_dx[d]
        i=0
        continue
    if (lst[r+dy[0]][c+dx[0]] == 1 or lst[r+dy[0]][c+dx[0]] == 2) and (lst[r+dy[1]][c+dx[1]] == 1 or lst[r+dy[1]][c+dx[1]] == 2) and (lst[r+dy[2]][c+dx[2]] == 1 or lst[r+dy[2]][c+dx[2]] == 2) and (lst[r+dy[3]][c+dx[3]] == 1 or lst[r+dy[3]][c+dx[3]] == 2) and  lst[r+back_dy[d]][c+back_dx[d]] == 1 :
        break
    
    if c+dx[d] < 0 or c+dx[d] >= m or r+dy[d] < 0 or r+dy[d] >= n or lst[r+dy[d]][c+dx[d]] == 1 or lst[r+dy[d]][c+dx[d]] == 2 :  #만약에 검사좌표가 범위를 벗어나면
        d-=1
        if d==-1 :
            d=3
        continue    # 방향 바꿔주고 continue
    x=c+dx[d]
    y=r+dy[d]
    if lst[y][x] == 0 :
        
        lst[y][x] = 2
        d-=1
        if d==-1 :
            d=3
        c,r=x,y
        cnt+=1
        i=0
        continue
    
    d-=1
    if d==-1 :
        d=3

print(cnt)