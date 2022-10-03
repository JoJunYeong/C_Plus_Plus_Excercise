/*  Volatile 키워드  */

/*
컴파일러의 최적화 옵션을 빼버리는 것입니다. 
gcc 에서는 단순히 최적화 옵션을 안주면 됩니다. 
Visual Studio 에서는 살짝 복잡한데, 프로젝트 속성의 C/C++ –> 최적화 에서 사용 안함을 선택하시면 됩니다. 
그런데, 최적화를 하지 않기에는 너무나 그 손실이 큽니다. 
최적화 옵션을 끄는 순간 다른 모든 코드들도 최적화를 하지 않겠다는 의미가 되거든요. 
이를 위해 volatile 키워드가 생겨났습니다.

#include <stdio.h>
typedef struct SENSOR {
  // 감지 안되면 0, 감지되면 1 이다.
  int sensor_flag;
  int data;
} SENSOR;

int main() {
  volatile SENSOR *sensor;
  // 값이 감지되지 않는 동안 계속 무한 루프를 돈다 
  while (!(sensor->sensor_flag)) {
  }
  printf("Data : %d \n", sensor->data);
}

이렇게 해준 순간 컴파일러는 sensor 에 대해 최적화를 수행하지 않게 됩니다. 
volatile 의 의미는 '변덕스러운' 이라는 의미를 가지고 있는데,
 sensor 에 volatile 키워드를 붙여준 순간 sensor->sensor_flag 의 값이 
 '변덕스럽게 변할 수 있기 때문' 에 이에 대한 최적화 작업들을 수행하지 말라 라는 의미가 됩니다. 
 따라서 컴파일러는 위 소스를 의미 그대로 컴파일 하게 되어 우리가 원하던 결과를 얻을 수 있게 됩니다.



*/














