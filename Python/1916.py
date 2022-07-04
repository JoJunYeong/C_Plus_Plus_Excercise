import sys
import heapq

input = sys.stdin.readline

city_num = int(input())
bus_num = int(input())
graph =[[] for _ in range(city_num+1)]
visited = [False] *  (city_num+1)
cities = [1e9 ]* (city_num+1)
for i in range(bus_num) :
    city1,city2,gajoong = map(int, input().split())
    graph[city1].append([gajoong,city2])
start_city, end_city = map(int,input().split())
present_city = start_city
cities[present_city] = 0 
wait_queue = []

heapq.heapify(wait_queue)
heapq.heappush(wait_queue,(0,start_city))

while wait_queue :

    gajoong, city = heapq.heappop(wait_queue)

    if cities[city] < gajoong :
        continue

    for next_city in graph[city] :

        if cities[next_city[1]] > (cities[city]+next_city[0]) :
            cities[next_city[1]] = cities[city]+next_city[0]
            heapq.heappush(wait_queue,(cities[next_city[1]],next_city[1]))

print(cities[end_city])






