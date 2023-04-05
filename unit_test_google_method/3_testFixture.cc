
class Calc{
    public:
        double Display() { return 0; }

        void Enter(double n) {}

        void PressPlus() {}
        void PressMinus() {}
        void PressEnter() {}

};


#include <gtest/gtest.h>

/*
    1. Test Fixture
    정의 : xUnit Test Framework에서 SUT를 실행하기 위해서 준비해야 하는
            모든것을 테스트 픽스쳐라고 한다.
            테스트 픽스쳐를 구성하는 모든 코드의 로직부분을 "픽스쳐 설치"라고 한다.
            주로 Arrange 단계에서 수행된다.

    2. Test Fixture 설치하는 방법 3가지
        1) Inline Fixture Setup
        : 모든 픽스쳐 설치를 테스트 케이스 안에서 수행한다.(모든 Test Case에서 Arrange를 같은 내용을 수행하는 것)
        장점 : 픽스쳐를 설치하는 과정과 검증의 로직이 하나의 테스트 케이스 함수 안에 존재하기 때문에 인과관계를 분석하기 쉽다.
        단점 : 모든 테스트 케이스 안에서 "테스트 코드 중복" 문제가 발생한다.

        2) Delegate Set Up (위임 설치)
        : 픽스쳐 설치에 관한 코드를 별도의 "Test 유틸리티 함수"를 통해 캡슐화 한다.
        => 명시적인 테스트 스위트 클래스를 만들어야(제공해야) 한다.

*/
#define SPEC(msg) printf("SPEC: " msg "\n")


// 명시적인 테스트 스위트 클래스
class CalcTest : public testing::Test {
    protected:
    // 구글 테스트에서 테스트 유틸리티 메소드를 제공할 때,
    // protected로 만들어야 하는 구조적인 이유를 아는것이 중요하다.
    // 만약에 private로 만든면, 자식 클래스에서 접근할 수 없기 때문이다.
        Calc* CreateCalc() { return new Calc; }
};

// - TEST
// class CalcTest_Plus : public ::testing::Test

// - TEST_F (명시적인 케이스)
// class CalcTest_Plus : public CalcTest
TEST_F(CalcTest, Plus)
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

}


TEST_F(CalcTest, PressMinus){

    // Arrange
    Calc* calc = new Calc;

    // Act
    calc->Enter(4);
    calc->PressMinus();
    calc->Enter(2);

    // Assert
    ASSERT_EQ(calc->Display(), 2) << "4-2 하였을 때";



}




