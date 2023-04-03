#include <vector>
#include <queue>
#include <utility>
#include <limits>

using namespace std;

vector<int> dijkstra(vector<vector<pair<int,int>>> &graph, int start){
    int n = graph.size();
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

        



    } 



}