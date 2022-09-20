// 함수에서 배열을 인자로 받기

// 여기에서 만들 함수는 배열을 인자로 받아서 그 배열의 각 원소의 값을 1씩 증가시키는 함수.

#include <stdio.h>

int add_number(int *parr);
int main() {
  int arr[3];
  int i;

  /* 사용자로 부터 3 개의 원소를 입력 받는다. */
  for (i = 0; i < 3; i++) {
    scanf("%d", &arr[i]);
  }

  add_number(arr);

  printf("배열의 각 원소 : %d, %d, %d \n", arr[0], arr[1], arr[2]);

  return 0;
}
int add_number(int *parr) {
  int i;
  for (i = 0; i < 3; i++) {
    printf("%d %p \n",parr[i], &parr[i]);
    parr[i]++;
  }
  return 0;
}

