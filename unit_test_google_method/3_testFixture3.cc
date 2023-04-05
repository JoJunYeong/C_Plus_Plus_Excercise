
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

        3) Implicit SetUp (암묵적 설치)
        : 여러 테스트 케이스 안에서 같은 테스트 픽스쳐의 설치/해체 코드를 암묵적으로 호출되는 함수를 통해서 처리한다.
        => 명시적인 테스트 스위트 클래스가 필요하다.
        장점 : 테스트 코드 중복을 제거하고, 불필요한 준비과정을 테스트 케이스 안에서 제거할 수 있다.
        단점 : 테스트 픽스쳐 설치 코드가 테스트 케이스 외부에 존재하기 때문에, 테스트 케이스 만으로 테스트 코드를 분석하기 어렵다.

    3. ASSERT_XX
    => 테스트 케이스 안에서 ASSERT가 실패할 경우,
       이후의 코드가 수행되지 않는다.

    4. xUnit Test Pattern 에서 테스트 케이스를 구성하는 방법
    => 4단계 테스트 패턴(Four Phase Test Pattern)
        1단계 : 테스트 픽스쳐를 설치하거나, 실제 결과를 관찰하기 위해
                필요한 것을 설정한다. => SetUp
        
        2단계 : SUT와 상호 작용한다.
        3단계 : 기대결과를 확인한다.
        4단계 : 테스트 픽스쳐를 해체해서, 테스트 케이스 시작 이전의 상태와 동일하게 만들어준다. => TearDown





*/
#define SPEC(msg) printf("SPEC: " msg "\n")


// 명시적인 테스트 스위트 클래스
class CalcTest : public testing::Test {
    protected:
        // 아래 작업을 해줌으로서 Arrange가 필요없게 되었다.
        // 그리고 class에서 설명을 바꾸더라도 SetUp안에서만 설정을 바꿔주면 되기 때문에 
        // 유지보수도 간단해졌다.
        Calc* calc = nullptr;
        void SetUp() override{
            std::cout <<"Setup" << std::endl;
            calc = new Calc;
        }

        void TearDown() override{
            std::cout << "TearDown" <<std::endl;
            delete calc;
        }
};

TEST_F(CalcTest, Plus)
{
    SPEC("2더하기 2를 하였을 때, 결과가 4가 제대로 나오는지 검증한다.");
    // Arrange
    // Calc* calc = new Calc;

    // Act
    calc->Enter(2);
    calc->PressPlus();
    calc->Enter(2);

    // Assert
    ASSERT_EQ(calc->Display(), 4) << "2+2 하였을 때";

}


TEST_F(CalcTest, PressMinus){

    // Arrange
    // Calc* calc = new Calc;

    // Act
    calc->Enter(4);
    calc->PressMinus();
    calc->Enter(2);

    // Assert
    ASSERT_EQ(calc->Display(), 2) << "4-2 하였을 때";



}




