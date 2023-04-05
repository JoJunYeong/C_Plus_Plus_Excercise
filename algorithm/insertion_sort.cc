/*
예시 문제: 정렬되어 있지 않은 정수 리스트를 입력 받아 이분 탐색을 사용하여 특정 값을 검색하려고 합니다. 
이를 위해 리스트를 정렬한 후 이분 탐색을 수행해야 합니다. 
선택 정렬과 삽입 정렬 두 가지 방법을 사용하여 리스트를 정렬한 후, 
이분 탐색으로 원하는 값을 찾아 인덱스를 반환하세요.

예시 입력 리스트: [5, 2, 8, 1, 9, 7]
찾을 값: 7
*/

#include <iostream>
#include <deque>

void insertionSort(std::deque <int> &deq){

    for(int i = 1 ; i < deq.size() ; i++){
        int key = deq[i];
        int j = i - 1;
        while(j >= 0 && deq[j] > key){
            deq[j+1] = deq[j];
            j--;
        }
        deq[j+1] = key;
    }
}


int main() {
    std::deque <int> deq = {8, 4, 3, 7, 6};
    insertionSort(deq);

    for (int i = 0; i < deq.size(); i++) {
        std::cout << deq[i] << " ";
    }

    return 0;
}



