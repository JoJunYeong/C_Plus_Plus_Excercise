// 지역변수와 전역변수, 정적변수
// 데이터 세그먼트에 대해서 알아본다.

// 지역변수와 전역변수에 대해서는 건너뛰고 정적변수에 대해서 알아보도록 하겠다.
#include <stdio.h>

int *function_(){
    static int a = 2;   // 놀라운 점은 function 을 실행하지 않더라도 a 라는 정적 변수는 이미 정의되어 있는 상태라는 것이다.
    return &a;
}

/*

유지훈2020-03-13T02:42:31.918Z
안녕하세요? 위의 본문 내용 중, 아래 예제 코드에 대해 질문이 있습니다.
아래 코드에서 function()와 function2() 안에서 static int how_many_called=0;으로 정적 변수 이름이 동일한데요, 
정적 변수를 선언하게 되면, 함수 호출 시 생성되는게 아니라 전역변수와 동일하게 프로그램 시작 시 생성되어 
data segment영역에 저장된다고 하셨는데요,
함수 호출과 상관없이 만들어지는데 변수 이름이 동일해도 괜찮나요?
두 변수가 이름도 같고 만들어지는 시기는 동일하지만, 다른 주소값을 가지며 서로 다른 scope안에서 정의되었고, 
해당 scope안에서만 접근 가능하기 때문에 가능한건가요? 

Jaebum Lee2020-03-28T05:01:54.839Z
네 다른 스코프에 정의된 변수들이기 때문에 컴파일러 입장에서는 다른 변수라 생각합니다.

*/

int function() {
  static int how_many_called = 0;

  how_many_called++;
  printf("function  called : %d \n", how_many_called);

  return 0;
}
int function2() {
  static int how_many_called = 0;

  how_many_called++;
  printf("function2 called : %d \n", how_many_called);

  return 0;
}

int main(){
    int *pa = function_();
    printf("%d\n", *pa);

    function();
    function2();
    function();
    function2();
    function2();
    function2();
    function();
    function();
    function2();
    return 0;
}

