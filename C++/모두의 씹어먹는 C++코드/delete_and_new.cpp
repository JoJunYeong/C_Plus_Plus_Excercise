// 프로그램이 정확하게 실행되기 위해서는 컴파일 시에 모든 변수의 주소값이 확정되어야만 했습니다. 
// 하지만, 이를 위해서는 프로그램에 많은 제약이 따르기 때문에 프로그램 실행 시에 자유롭게 할당하고 해제할 수 있는 
// 힙(heap) 이라는 공간이 따로 생겼습니다.

// 컴파일러에 의해 어느정도 안정성이 보장되는 스택(stack) 과는 다르게 
// 힙은 사용자가 스스로 제어해야 하는 부분인 만큼 책임이 따릅니다.

// C 언어에서는 malloc 과 free 함수를 지원하여 힙 상에서의 메모리 할당을 지원하였습니다. 
// C++ 에서도 마찬가지로 malloc 과 free 함수를 사용할 수 있습니다.
// 하지만, 언어 차원에서 지원하는 것으로 바로 new 와 delete 라고 할 수 있습니다. 
// new 는 말 그대로 malloc 과 대응되는 것으로 메모리를 할당하고 
// delete 는 free 에 대응되는 것으로 메모리를 해제합니다. 


// #include <iostream>

// int main(void){

//     int arr_size;
//     std::cout << "input array size";
//     std::cin >> arr_size;
//     int *list = new int[arr_size];
//     for(int i = 0 ; i < arr_size ; i++)
//         std::cin >> list[i];
//     for(int i =0; i < arr_size ;i++)
//         std::cout << i << "th elements of list : " << list[i] << std::endl;
    
//     delete[] list;


//     return 0;
// }



// 돌아온 마이펫 코드

#include <iostream>




void play(){



}

void show_stat(){

}


struct Animal{
    char name[30];
    int age;
    int health;
    int food;
    int clean;
}Animal;


int main(){
    


    struct Animal *list[30] = new struct[]




    return 0;
}








