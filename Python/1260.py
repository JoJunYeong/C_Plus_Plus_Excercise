from collections import defaultdict,deque

n,m,v = map(int,input().split())
lst=[]
# DFS - 깊이 우선 탐색 -> 스택을 이용. 파이썬에서 리스트는 스택으로 구현되어 있음!

list_graph = defaultdict(list)

for i in range(m) :
    a,b = map(int,input().split())
    list_graph[a].append(b)
    list_graph[b].append(a)

#DFS
def dfs(graph, start):
    result, visit= deque(), deque()
    lst=[]
    visit.append(start)
    
    while visit:
        node = visit.pop()
        if node not in result:
            result.append(node)
            graph[node].sort(reverse=True)
            visit.extend(graph[node])
    lst=result
    return lst 

#Test Code


for i in dfs(list_graph, v) :
    print(i,'',end='')
print('')



# BFS
def bfs(graph,start):
    result,visit = deque(), deque()
    visit.append(start)
    graph[start].sort(reverse = False)
    while visit :
        node = visit.pop()
        if node not in result: 
            result.append(node)
            graph[node].sort(reverse = False)
            visit.extendleft(graph[node])
        # print('visit=',visit,'result=',result)
    return result



for i in bfs(list_graph,v) :
    print(i,'',end='')
print('')
