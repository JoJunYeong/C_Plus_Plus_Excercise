from collections import deque
import sys
sys.setrecursionlimit(100000)

itera = int(sys.stdin.readline())

for qq in range(itera) :

    a,b,c = map(int,input().split())
    dx=[-1,1,0,0]   # 좌, 우 이동 dx좌표값
    dy=[0,0,-1,1]   # 상, 하 이동 dy좌표값
    lst=[]
    lst2=list(list(map(int, input().split())) for _ in range(c))
    for i in range(a) :     # 배추밭 초기화 
        lst.append([])
        for j in range(b) :
            if [i,j] in lst2 :
                lst[i].append(1)
            else :
                lst[i].append(0)

    # 배추밭 돌아댕기면서 상하좌우 검사하면서 벌레가 있는곳은 cnt해주기
    dq_result=deque()
    for i in range(a) :
        for j in range(b) :
            if lst[i][j] != 0 and lst[i][j] == 1 :
                dq_x=deque()
                dq_y=deque()
                dq_x.append(j)
                dq_y.append(i)
                while dq_x :
                    jj=dq_x.popleft()
                    ii=dq_y.popleft()
                    if [ii,jj] not in dq_result :                           
                                dq_result.append([ii,jj])
                    for k in range(4) :
                        x=jj+dx[k]
                        y=ii+dy[k]
                        if x>=b or x<0 or y>=a or y<0 :
                            continue
                        if lst[y][x] == 1 and [y,x] not in dq_result:
                            dq_x.append(x)
                            dq_y.append(y)
                            lst[y][x] = lst[ii][jj]+1
   
    cnt=0
    for i in range(a) :
        for j in range(b) :
            if lst[i][j]==1 :
                cnt+=1
    print(cnt)                
                            

    




