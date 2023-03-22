/*
예시 문제: 정렬되어 있지 않은 정수 리스트를 입력 받아 이분 탐색을 사용하여 특정 값을 검색하려고 합니다. 
이를 위해 리스트를 정렬한 후 이분 탐색을 수행해야 합니다. 
선택 정렬과 삽입 정렬 두 가지 방법을 사용하여 리스트를 정렬한 후, 
이분 탐색으로 원하는 값을 찾아 인덱스를 반환하세요.

예시 입력 리스트: [5, 2, 8, 1, 9, 7]
찾을 값: 7
*/

#include <cstdio>
#include <deque>
#include <iostream>

void selection_sort(std::deque <int> &deq){

    int n = deq.size();
    for(int i = 0 ; i < n ; i++){
        int target_val = deq[i];
        int min_val = target_val;
        int min_idx = i;
        for(int j = i+1 ; j < n ; j++){
            if(deq[j] < min_val){
                min_val = deq[j];
                min_idx = j;
            }
        }
        deq[i] = min_val;
        deq[min_idx] = target_val;
    }
}


int main(void){
    std::deque <int> deq = {64, 34, 25, 12, 22, 11, 90};

    selection_sort(deq);

    for(int i : deq){
        std::cout << i << " ";
    }
    std::cout << std::endl;
    return 0;
}




