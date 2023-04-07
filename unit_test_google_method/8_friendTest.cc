#include <string>
#include <gtest/gtest.h>
class User{
    private:
        int age = 10;
        // 문제 : 테스트에서 확인해야 되는 상태가
        //          private이라서 테스트하지 못한 요구사항이 존재하게 된다.

    public:
        int GetAge() const { return age; }

        void NextYear() { ++age; }

        // 핵심코드
        FRIEND_TEST(UserTest, NextYear);

};




TEST(UserTest, NextYear){

    User user;

    user.NextYear();

    // public인 GetAge는 접근가능하지만, private에는 접근할 수다 없다.
    // 그래서 ifdef를 통해 private을 public으로 바꾸는 아주 멍청한 짓들을 많이 했는데,
    // 이걸 해결하기 위해 Google에서 Friend Test 라는방법을 만들어냈다. 
    // 그러나 단점은 이렇게 하게 되면, google에 대한 의존도가 올라간다.
    /*
        => C++의 friend 기능을 이용해서
            특정한 테스트케이스가 SUT의 privatre에 접근할 수 있다.
        => SUT에 google test 플에임 워크에 대한 의존성이 생긴다.

        Clean Code 조건
        1. 테스트 용이성 : 제품 코드는 테스트가 용이해야 한다.
        2. 테스트 되지않은 private메소드보다 테스트된 public이 더 안전하다.
        3. private메소드는 public 메소드의 가독성을 높이기 위해 사용해야 한다.
            public 메소드를 검증하면 private메소드도 자연스럽게 검증 될 것이다.
    
    
    */
    EXPECT_EQ(user.GetAge(),11);


}



