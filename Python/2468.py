
# BFS 를 써야하는 문제같은 경우 result와 visit의 두가지 deque를 써서 그 안의 요소가 있냐 없냐
# 이렇게 쓰는것보다 같은 배열만큼의 T/F를 가진 부울 배열을 만들어서 이걸로 방문표시를 사용한다.
# 그러면 시간복잡도가 굉장히 낮아진다
# 특히 visit안에 그리고 result deque안에 요소가 1000개씩 들어있는
# 100000*100000배열이라면 not in 이 갖는 시간복잡도가 이해가 된다.
# 결론은 BFS에서 not in 왠만하면 쓰지 말자

from collections import deque
import sys

sys.setrecursionlimit(100000)
a=int(input())
map_original = list(list(map(int, sys.stdin.readline().split())) for _ in range(a))
lst=[]
lst2=[]
for i in range(a) :
    lst2.append([])
    for j in range(a) :
        lst2[i].append(False)
        if map_original[i][j] not in lst :
            lst.append(map_original[i][j])

dx = [1,-1,0,0] # 오른쪽, 왼쪽 이동이다
dy = [0,0,1,-1] # 아래, 위 이동이다
maxi=0
for q in lst :
    cnt=0
    lst3=[item[:] for item in lst2]
    visited = [item[:] for item in lst2]
    visit = deque()
    for i in range(a) :
        for j in range(a) :
            if map_original[i][j] > q and lst3[i][j] == False :
                cnt += 1
                # print(f'[i][j]=[{i}][{j}]')
                visit.append([i,j])
                visited[i][j] = True
                while visit :
                    ii,jj = visit.popleft()
                    lst3[ii][jj] = True
                    for k in range(4) :
                        x=jj+dx[k]
                        y=ii+dy[k]       
                        if 0<=x<a and 0<=y<a :      
                            if map_original[y][x] > q and visited[y][x]==False and lst3[y][x]==False :
                                visit.append([y,x]) 
                                visited[y][x] = True  

    maxi=max(maxi,cnt)
if maxi==0 :
    print(1)
else :
    print(maxi)

