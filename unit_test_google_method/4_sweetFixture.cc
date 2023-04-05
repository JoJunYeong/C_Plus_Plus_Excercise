
#include <string>
#include <unistd.h>
#include <iostream>

class Terminal {
    public:
        void Connect() { sleep(2); }
        void Disconnect() { sleep(2); }

        void Login(const std::string& id, const std::string& password) {}
        void Logout() { }

        bool IsLogin() const { return false;}
};


#include <gtest/gtest.h>

// connect와 disconnect가 느리다고 가정했을 때, 상황
/*
문제점 : SetUp / TearDown 이 느려서 (픽스쳐의 설치와 해체가 느려서)
테스트케이스가 추가될대마다 전체적인 테스트의 수행 시간이 늘어나는 문제가 발생한다.
=> 이를 Slow Test 문제라고 한다.

Slow Test문제
    1) 테스트가 너무 느려서, 테스트를 수행하는 개발자의 생산성을 떨어뜨린다.
    2) 테스트가 너무 느려서, 아무고 코드가 변경되어도 테스트를 수행하지 않는다.

해결방법 : 스위트 픽스쳐
"스위트 픽스쳐 = 공유 픽스쳐 전략"
정의 : 모든 테스트 케이스가 동일한 하나의 픽스쳐를 공유한다.
        성능은 빠르게 동작하지만, 이정의 테스트 케이스가 픽스쳐를 망가트리면
        이후의 테스트의 결과를 신뢰할 수 없는 "변덕스러운 테스트 문제가 발생할 수 있다."

*/




// 명시적인 Test sweet class 생성
class TerminalTest : public testing::Test{
    protected:
        Terminal* term = nullptr;

        static void SetUpTestSuite(){
            std::cout << "SetUpTestSuite" << std::endl;
        }
        static void TearDownTestSuite(){
            std::cout << "TearDownTestSuite" << std::endl;
        }

        void SetUp() override {
           term = new Terminal;
           term->Connect();
        }
        void TearDown() override {
            term->Disconnect();
            delete term;
        }

};



TEST_F(TerminalTest, Login){
   

    term->Login("test_id", "test_password");
    ASSERT_TRUE(term->IsLogin()) << "로그인 하였을 떄";

}

TEST_F(TerminalTest, Logout){
   
    term->Login("test_id", "test_password");
    term->Logout();

    ASSERT_TRUE(term->IsLogin()) << "로그인 하였을 떄";


}

