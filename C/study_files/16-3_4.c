// 멤버를 쉽게 초기화 하기

#include <stdio.h>

struct Human{
    int age;
    int height;
    int weight;
    int gender;
};

int Print_Status(struct Human human);

int main() {

    struct Human Adam = {31,182,75,0};
    struct Human Eve = {27, 166,48,1};

    Print_Status(Adam);
    Print_Status(Eve);

    return 0;
}

int Print_Status(struct Human human){
    if (human.gender == 0) 
        printf("Male \n");
    else 
        printf("Female \n");
    
    printf("AGE : %d / Height : %d / Weight : %d \n", human.age, human.height, human.weight);

    if(human.gender == 0 && human.height >= 100)
        printf("He is a winner!! \n");
    else if(human.gender == 0 && human.height < 100)
        printf("He is a loser!! \n");

    printf("---------------------------------\n");
    return 0;
}




