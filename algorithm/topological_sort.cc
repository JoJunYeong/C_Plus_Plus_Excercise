#include <iostream>
#include <deque>

std::deque<std::deque<int>> adj;
std::deque<int> indegree;

std::deque<int> topological_sort(std::deque<std::deque<int>> &adj_list, std::deque<int> &in_degree){

    int n = adj_list.size();
    std::deque<int> sorted_list;
    std::deque<int> q;

    for(int i = 1; i < n ; i++){
        if(in_degree[i] == 0){
            q.push_back(i);
        }
    }

    while(!q.empty()){
        int node = q.front();
        q.pop_front();
        sorted_list.push_back(node);

        for(int next_node : adj_list[node]) {
            --in_degree[next_node];
            if(in_degree[next_node] == 0) {
                q.push_back(next_node);
            }
        }
    }

    return sorted_list;
}


int main(){

    int V,E;
    std::cout<< "Enter the number of vertices(V) and edges(E): ";
    std::cin >> V >> E;

    std::deque<std::deque<int>> adj_list(V+1);
    std::deque<int> in_degree(V+1,0);

    std::cout << "Enter the edges as pairs of vertices:" << std::endl;
    for(int i = 0; i < E ; i++){
        int from, to;
        std::cin >> from >> to;
        adj_list[from].push_back(to);
        ++in_degree[to];
    }


    std::deque<int> sorted_list = topological_sort(adj_list,in_degree);

    std::cout << "Topological sorted order:" << std::endl;
    for(int node : sorted_list){
        std::cout << node << " ";
    }
    
    return 0;
}