// 2_3A.cc
// SUT(System Under Test, 테스트 대상 시스템)
//  => CUT(Class Under Test)
//     CUT(Code Under Test)



class Calc{
    public:
        double Display() { return 0; }

        void Enter(double n) {}

        void PressPlus() {}
        void PressEnter() {}

};


#include <gtest/gtest.h>
// Google Test Framework는 1.8 , 1.10버전에서 획기적인 발전을 이루었다.
// 1.8 버전에서는 - Google Mock 프로젝트가 흡수되었다.
// 1.10버전에서 구글 테스트의 내부용어와 xUnit Test Framework용어가 통합되었다.


// 2. 테스트 케이스를 구성하는 방법
//   1) TEST(테스트 스위트 이름, 테스트 케이스 이름)
//    => 일반적으로 테스트 대상 클래스의 이름의 뒤에 Test/Spec 을 붙이는 형태로
//       테스트 스위트를 구성한다.
// 예시
// TEST(CalcTest, Plus) { }
// TEST(CalcTest, Minus) { }

#if 0
// 두번쨰 예시
TEST(ClacTest, Plus){
    // 테스트 케이스를 만드는 중일때(Empty인 Case)는 의도적으로 Fail을 return 시킨다.
    // FAIL();
    // 그러나 그냥 실패만 하는것이 아니라, 실패의 이유를 명시하는 것이 중요하다.
    FAIL() << "작성중입니다.";
}
#endif

// 그럼 어떤식으로 테스트를 작성해야될지 막막할 때가 있다.
// 이럴때 사용하기 좋은 template이 3A이다.
// 3A
// - Arrange(Given): 테스트 대상 코드(SUT)를 초기화하고, 필요한 경우 설정하고 준비한다.
// - Act(When) : 테스트 대상 코드에 작용(함수, 메소드)을 가합니다.
// - Assert(Then): 기대하는 바를 단언합니다.

/*
3. 테스트 케이스의 품질
    1) 가독성
    - Test가 실패하였을 떄, 실패의 원인이 오류 메세지를 통해 드러나는가?
    - Testcase의 이름을 최대한 자세하게 사용하자. 그게 안되면 SPEC을 사용하자.
        ex) python의 경우는 (Spoke) 아예 이름을 문자열로 "~~했을 때 ~~상황의 ~~ 결과기대" 이런느낌으로 하지만
            c++은 그런것이 안되므로
            SPEC이라는 define을 만들어서 사용한다.

    2) 유지보수성
    - test code도 유지보수의 대상입니다.
    - test code의 유지보수의 비용이 최소화 되어야 합니다.
        "test code 안에서 제어 구문의 사용을 최소화 해야 합니다."


    3) 신뢰성





4. BDD(Behavior Driven Development, 행위 주도 개발) 
    1) 가독성을 중요시하게 여김 => 용어를 좀 더 문장에 가깝게 사용하는 것을 지향합니다.
    2) 행위 검즘
    3) 대표적으로 Python은 SPOKE 프레임워크가, JS는 Should.js 프레임워크가 BDD를 추구한다.

*/




#define SPEC(msg) printf("SPEC: " msg "\n")


TEST(CalcTest, Plus)
{
    SPEC("2더하기 2를 하였을 때, 결과가 4가 제대로 나오는지 검증한다.");
    // Arrange
    Calc* calc = new Calc;

    // Act
    calc->Enter(2);
    calc->PressPlus();
    calc->Enter(2);

    // Assert
    ASSERT_EQ(calc->Display(), 4) << "2+2 하였을 때";

#if 0
    if(calc->Display() == 4){
        SUCCEED();
    } else {
        FAIL() << "2+2 하였을 때, 기대한 결과와 다릅니다.";
    }
#endif
}

