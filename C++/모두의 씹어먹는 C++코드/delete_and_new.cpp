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



// typedef를 사용하면 별칭을 사용할 수 있다.
// 예를들면 아래 CreateAnimal에서 Animal *animal 이렇게 한 것과 같은 원리인 것 같다.
// 아무래도 이 구조체를 계속 불러서 사용하다 보니까 별칭으로 지정해서 불러야 되는 경우가 생기는 것 같다.
typedef struct Animal{
    char name[30];
    int age;
    int health;
    int food;
    int clean;
}Animal;



void Play(Animal *animal){
    animal->food -= 20;
    animal->clean -= 30;
    animal->health += 10;
}

void OneDayPass(Animal *animal){
    animal->clean -= 20;
    animal->food -= 30;
    animal->health -= 10;
}


void ShowStat(Animal *animal){
    std::cout << animal->name << "의 상태" << std::endl;
    std::cout << "체력 :   " << animal -> health << std::endl;
    std::cout << "배부름 :   " << animal -> food << std::endl;
    std::cout << "청결 :     " << animal -> clean << std::endl;

}

void CreateAnimal(Animal *animal){
    std::cout << "동물의 이름?" ;
    std::cin >> animal->name;
    std::cout << "동물의 나이?";
    std::cin >> animal->age;
    
    animal->food = 100;
    animal->health = 100;
    animal->clean = 100;
    
}




int main(){
    

    struct Animal *list[30] = new struct[]




    return 0;
}








