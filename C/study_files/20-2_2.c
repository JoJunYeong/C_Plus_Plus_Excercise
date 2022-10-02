
/*    노드 (node)    */

#include <stdio.h>
#include <stdlib.h>

struct Node* InsertNode(struct Node* current, int data);
void DestroyNode(struct Node* destroy, struct Node* head);
struct Node* CreateNode(int data);
void PrintNodeFrom(struct Node* from);

struct Node{
    int data;   // 데이터
    struct Node* nextNode; // 다음 노드를 가리키는 부분
};

int main(){
    struct Node* Node1 = CreateNode(100);
    struct Node* Node2 = InsertNode(Node1, 200);
    struct Node* Node3 = InsertNode(Node2, 300);
    // Node2 뒤에 Node4 넣기
    struct Node* Node4 = InsertNode(Node2, 400);

    PrintNodeFrom(Node1);

    return 0;
}

void PrintNodeFrom(struct Node* from){
    // from이 NULL 일 때까지, 
    // 즉 끝 부분에 도달 할 때 까지 출력
    while(from){
        printf("노드의 데이터 : %d \n", from -> data);
        from = from -> nextNode;
    }
}

// current라는 노드 뒤에 노드를 새로 만들어 넣는 함수
struct Node* InsertNode(struct Node* current, int data){
    // current 노드가 가리키고 있던 다음 노드가 after이다.
    struct Node* after = current->nextNode;

    // 새로운 Node를 생성한다.
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

    // 새 Node에 값으 ㄹ넣어준다.
    newNode->data = data;
    newNode->nextNode = after;

    // current는 이제 newNode를 가리키게 된다.
    current->nextNode = newNode;

    return newNode;
}

// 선택된 노드를 파괴하는 함수
void DestroyNode(struct Node* destroy, struct Node* head){
    struct Node* next = head;
    if(destroy == head){
        free(destroy);
        return ;
    }

    while(next){
        if(next->nextNode == destroy)
            next->nextNode = destroy->nextNode;
        next = next->nextNode;
    }
    free(destroy);

}

// 새 노드를 만드는 함수
struct Node* CreateNode(int data){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

    newNode->data = data;
    newNode->nextNode = NULL;

    return newNode;

}






