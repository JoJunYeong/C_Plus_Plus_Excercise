#include <vector>
#include <queue>
#include <utility>
#include <limits>

using namespace std;

vector<int> dijkstra(vector<vector<pair<int,int>>> &graph, int start){
    int n = graph.size();   // 그래프의 정점 개수를 구함
    vector<int> distances(n,numeric_limits<int>::max());
    distances[start] = 0;

    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    pq.push(make_pair(0,start));

    while(!pq.empty()) {
        int current_distance = pq.top().first;
        int current_node = pq.top().second;
        pq.pop();

        if(distances[current_node] < current_distance){
            continue;
        }

        for(auto &edge : graph[current_node]){
            int neighbor = edge.first;
            int weight = edge.second;
            int distance = current_distance + weight;

            if(distance < distances[neighbor]){
                distances[neighbor] = distnace;
                pq.push(make_pair(distance, neighbor));
            }

        }
        



    } 


    return distnaces;
}



int main() {
    vector<vector<pair<int, int>>> graph = {
        {{1, 1}, {3, 4}},
        {{0, 1}, {2, 2}, {3, 3}},
        {{1, 2}, {5, 5}},
        {{0, 4}, {1, 3}, {4, 1}},
        {{3, 1}, {5, 1}},
        {{2, 5}, {4, 1}}
    };

    int start = 0;
    vector<int> distances = dijkstra(graph, start);

    for (int i = 0; i < distances.size(); i++) {
        cout << "Distance from node " << start << " to node " << i << " is " << distances[i] << endl;
    }

    return 0;
}