#include <stdio.h>
int main() {
  int i;
  scanf("%d", &i);

  if (i & 1)  // 이 수가 홀수인가
  {
    printf("%d 는 홀수 입니다 \n", i);
  } else {
    printf("%d 는 짝수 입니다 \n", i);
  }
  return 0;
}