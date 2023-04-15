/*
    Google test의 기능이다.
    정의: 모든 테스트의 과정에서 수행해야 하는 작업을 정의할 수 있다.
    
*/

#include <gtest/gtest.h>

TEST(SampleTest,foo) {}
TEST(SampleTest,goo) {}

// 테스트 리스너를 만드는 방법
class MyTestListner : public testing::TestEventListener{

};

/*
    원하는 함수만 구현하고 싶다면,
    testing::EmptyTestEventListener를 상속하면, 원하는 기능만 재정의할 수 있다.

*/

class MyTestEventListener : public testing::EmptyTestEventListener{ 
    public:
        void OnTestProgramStart(const testing::UnitTest& unit_test) override{
            std::cout << __func__ << std::endl;
        }
        void OnTestProgramEnd(const testing::UnitTest& unit_test) override{
            std::cout << __func__ << std::endl;
        }

        void OnTestSuiteStart(const testing::TestSuite& test_case) override {

        }
        void OnTestSuiteEnd(const testing::TestSuite& test_case) override {

        }


};


/*
    2. 테스트 리스너를 등록하는 방법
    => main을 직접 정의해서 등록해야 한다.
*/

int main(int argc, char** argv){
    testing::InitGoogleTest(&argc, argv);

    testing::TestEventListeners& listeners = testing::UnitTest::GetInstance()->listeners();
    listeners.Append(new MyTestEventListener);

    // google test의 기본 프린터를 제거할 수 있습니다.
    delete listeners.Release(listeners.default_result_printer());

    return RUN_ALL_TESTS();
}


