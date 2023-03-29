

from collections import deque, defaultdict

def topological_sort(n,adj,indegree):
    #indegree = 그래프에서 들어오는 화살표를 뜻함    
    q = deque()
    sorted_list = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        curr = q.popleft()
        print(curr, end=" ")
        
        for next_node in adj[curr]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                q.append(next_node)
                

n=5
adj = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [4],
    4: []
}
indegree = [0, 1, 2, 1, 1]

topological_sort(n, adj, indegree)       








