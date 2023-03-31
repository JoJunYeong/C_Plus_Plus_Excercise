/* 1차원 배열 & 2차원 배열 동적할당 */
/* malloc 함수의 이해  */


#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  int SizeOfArray;
  int *arr;

  printf("만들고 싶은 배열의 원소의 수 : ");
  scanf("%d", &SizeOfArray);

  arr = (int *)malloc(sizeof(int) * SizeOfArray);
  // int arr[SizeOfArray] 와 동일한 작업을 한 크기의 배열 생성
  // malloc == memory allocation 
  // malloc 함수의 return 형은 void * 이므로 앞에 강제 형변환을 해주어야 한다.
  // malloc 함수는 heap 영역에 할당이 되는데, heap영역은 사용자가 추후에 값을 지정해 줄 수 있는 영역을 뜻한다.
  

  free(arr);

  return 0;
}




