
import sys
from collections import deque


sys.setrecursionlimit(100000000)
input = sys.stdin.readline

end,number = map(int, input().split())

graph = {}

for i in range(number) :
    a,b,gajoong = map(int,input().split())
    if a not in graph :
        graph[a]=[[b,gajoong]]
    else :
        graph[a]+=[[b,gajoong]]
    
    if b not in graph :
        graph[b]=[[a,gajoong]]
    else :
        graph[b]+=[[a,gajoong]]

must_pass1,must_pass2 = map(int,input().split())

wait = deque()
minn=10000000000000
visited =[False]*end
cnt =0 
def bfs(node_num, gajoon, wait,visited) :
    global cnt
    global end
    global minn
    for i in range(len(graph[node_num])) :
        if graph[node_num][i] not in wait :
            wait.append(graph[node_num][i])
   
    while wait :
        print(f'cnt={cnt}')
        print(f'wait={wait}')
        print(f'visited={visited}')
        cnt+=1
        if cnt >= 20 :
            print('break1')
            break
        node,gajoong_chi = wait.pop()
        new_gajoong = gajoong_chi+gajoong
        
        
        # print(visited)
        if node == end :
            if visited[must_pass1-1] == True and  visited[must_pass2-1] == True : 
                if minn > new_gajoong :
                    minn = new_gajoong
                    print(f'node={node}, new_gajoong={new_gajoong}')
                    print(f'minn={minn}')
                    break

        else :
            print('enter')
            bfs(node,new_gajoong,wait,visited)
        visited[node-1] = True

bfs(1,0,wait,visited)
print(minn)


