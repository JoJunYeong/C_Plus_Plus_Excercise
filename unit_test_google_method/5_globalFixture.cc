// 전역 픽스쳐
#include <iostream>
#include <gtest/gtest.h>
/*
1. 전역 픽스쳐
    - xUnit Test Framework의 기능이 아니다.
    => Google Test 고유의 기능이다.
    => 프로그램의 시작/종료에서 픽스쳐를 설치하고, 해체하는 기능을 제공할 수 있다.

2. 전역 픽스쳐 설치 방법
    1) testing::Environment를 상속해서
       설치와 해체코드를 작성한다.
    

*/

TEST(SampleTest, First) {}
TEST(SampleTest, Second) {}

TEST(ImageProcessorTest, ResizeImage) {}




class MyTestEnvironment : public testing::Environment{
    public:
        void SetUp() override{
            std::cout << "MyTestEnvironment SetUp()" << std::endl;
        }
        void TearDown() override{
            std::cout << "MyTestEnvironment TearDown()" << std::endl;
        }


};



class MyTestEnvironment2 : public testing::Environment{
    public:
        void SetUp() override{
            std::cout << "MyTestEnvironment2 SetUp()" << std::endl;
        }
        void TearDown() override{
            std::cout << "MyTestEnvironment2 TearDown()" << std::endl;
        }


};

// 등록하는 방법 2가지
// 주의사항 : 객체는 항상 new로 생성해야 한다.

#if 0
MyTestEnvironment myTestEnv;

//  1) main을 직접 정의한 경우
int main(int argc, char** argv){

    testing::InitGoogleTest(&argc, argv);
    
    testing::AddGlobalTestEnvironment(new MyTestEnvironment);
    testing::AddGlobalTestEnvironment(new MyTestEnvironment2);
    
    // testing::AddGlobalTestEnvironment(&myTestEnv);  // 이러면 안된다.

    return RUN_ALL_TESTS();

}
#endif
// 순서가 중요한 경우 main을 이용해서 test환경을 수행하면 된다.
// 위의 이유때문에 main을 이용한 방법을 많이 이용한다.




//  2) main을 정의하지 않는 경우(권장하지 않는 방법)
//  전역변수가 main 함수 이전에 초기화되는 특성을 이용한다.

// test1.cc
testing::Environment* myEnv = testing::AddGlobalTestEnvironment(new MyTestEnvironment);


// test2.cc
testing::Environment* myEnv2 = testing::AddGlobalTestEnvironment(new MyTestEnvironment2);

// C++ 표준에서는 각 파일의 전역 객체의 초기화/파괴 순서가 정해져 있지 않다.
// 2번의 방법은 순서가 제어되는것처럼 보이지만, 실제로는 순서가 코드에 
// 적힌 순서대로 되지 않는다.





/*
    픽스처에 대한 정리
    1) Test Fixture
    => 테스트 케이스 단위에서의 SetUp / TearDown
    => xUnit Test Framework

    2) Suite Fixture
    => 테스트 단위에서의 SetUp / TearDown
    => xUnit Test Framework

    3) Google Fixture
    => 프로그램 단위에서의 SetUp / TearDown
    => Google Test Framework


*/


