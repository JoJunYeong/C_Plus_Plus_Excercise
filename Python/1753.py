import heapq, sys

input = sys.stdin.readline

dot_num, line_num = map(int, input().split())
start_num = int(input())
graph=[[] for _ in range(dot_num+1)]
gajoong_status=[1e9]*(dot_num+1)

for i in range(line_num):
    dot1,dot2,gajoong = map(int, input().split())
    graph[dot1].append((gajoong,dot2))

wait_queue=[]
heapq.heapify(wait_queue)
heapq.heappush(wait_queue,(0,start_num))
print(graph)
while wait_queue :
    gajoong, present_dot = heapq.heappop(wait_queue)
    
    if gajoong_status[present_dot] < gajoong :
        continue
    gajoong_status[present_dot]=gajoong
    for next_dot_status in graph[present_dot] :
        if gajoong_status[next_dot_status[1]] > gajoong_status[present_dot] + next_dot_status[0] :
            gajoong_status[next_dot_status[1]] = gajoong_status[present_dot] + next_dot_status[0]
            heapq.heappush(wait_queue,(gajoong_status[next_dot_status[1]],next_dot_status[1]))
        print(f'wait_queue={wait_queue}')
        print(f'next_dot_status={next_dot_status}')
        print(f'gajoong_status={gajoong_status}\n')

# print(f'gajoong_status={gajoong_status}')

for i in range(1,dot_num+1) :
    if gajoong_status[i] == 1e9 :
        print('INF')
    else :
        print(gajoong_status[i])





