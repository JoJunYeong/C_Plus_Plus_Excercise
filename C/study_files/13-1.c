// 함수의 필요성, 함수의 의미, 함수의 인자, 함수의 리턴값, 함수 내부에서 선언된 변수에 대해 알아보자.

#include <stdio.h>
/* 보통 C 언어에서, 좋은 함수의 이름은 그 함수가
무슨 작업을 하는지 명확히 하는 것이다. 수학에서는
f(x), g(x) 로 막 정하지만, C 언어에서는 그 함수가 하는
작업을 설명해주는 이름을 정하는 것이 좋다. */
int print_hello() {
  printf("Hello!! \n");
  return 0;
}

int MagicBox(int a){
    return a+4;
}


int main() {
  printf("함수를 불러보자 : ");
  print_hello();

  printf("또 부를까? ");
  print_hello();
  return 0;
}