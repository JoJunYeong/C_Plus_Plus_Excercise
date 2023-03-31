/*  typedef, volatile, #pragma  */

/* 루저 위너 판별*/
/* typedef 의 이용 */
// typedef (이름을 새로 부여하고자하는 타입) (새로 준 타입의 이름)
// typedef (struct HUMAN) (Human);
// 위와같이 하고 나면 아래 두 문장은 동일한 문장이 된다.
// struct HUMAN a;
// Human a;

#include <stdio.h>
struct HUMAN {
  int age;
  int height;
  int weight;
  int gender;
};

typedef struct HUMAN Human;
int Print_Status(Human human);
int main() {
  Human Adam = {31, 182, 75, 0};
  Human Eve = {27, 166, 48, 1};

  Print_Status(Adam);
  Print_Status(Eve);
}

int Print_Status(Human human) {
  if (human.gender == 0) {
    printf("MALE \n");
  } else {
    printf("FEMALE \n");
  }

  printf("AGE : %d / Height : %d / Weight : %d \n", human.age, human.height,
         human.weight);

  if (human.gender == 0 && human.height >= 180) {
    printf("HE IS A WINNER!! \n");
  } else if (human.gender == 0 && human.height < 180) {
    printf("HE IS A LOSER!! \n");
  }

  printf("------------------------------------------- \n");

  return 0;
}





