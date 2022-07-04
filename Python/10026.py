from collections import deque
import sys

input = sys.stdin.readline

a=int(input())

map_original = list(list(input())for _ in range(a))
map_another = []
for i in range(a) :
    map_another.append([])
    for j in range(a) :
        if map_original[i][j] == "G" :
            map_another[i].append("R")
        else :
            map_another[i].append(map_original[i][j])

# print(map_another)
map_visited_normal = list([False]*a for _ in range(a))
map_visited_another = list([False]*a for _ in range(a))
wait = deque()

# bfs 풀이방식 접근
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt_normal_max, cnt_another_max = 0,0
wait_coordi=deque()

for i in range(a) :
    for j in range(a) :
        if map_visited_normal[i][j] == False :
            cnt_normal_max+=1
            wait.append([i,j,map_original[i][j]])
            while wait :
                # print(wait)
                y,x,rgb = wait.popleft()
                for z in range(4) :
                    xx = x+dx[z]
                    yy = y+dy[z]
                    if 0<= xx < a and 0 <= yy < a :
                        if rgb == map_original[yy][xx] and [yy,xx] not in wait_coordi :  
                            wait.append([yy,xx,rgb])
                            wait_coordi.append([yy,xx])
                map_visited_normal[y][x] = True
            # print(map_visited_normal)
wait.clear()
wait_coordi.clear()
for i in range(a) :
    for j in range(a) :
        if map_visited_another[i][j] == False :
            cnt_another_max+=1
            wait.append([i,j,map_another[i][j]])
            while wait :
                # print(wait)
                y,x,rgb = wait.popleft()
                for z in range(4) :
                    xx = x+dx[z]
                    yy = y+dy[z]
                    if 0<= xx < a and 0 <= yy < a :
                        if rgb == map_another[yy][xx] and [yy,xx] not in wait_coordi :  
                            wait.append([yy,xx,rgb])
                            wait_coordi.append([yy,xx])
                map_visited_another[y][x] = True
            # print(map_visited_normal)


print(f'{cnt_normal_max} {cnt_another_max}')


