
class User{

    private:
        int age = 10;

    protected:
        int GetAge() const { return age; }

    public:
        void NextYear() { ++age; }
};

#include <gtest/gtest.h>

/*
    테스트에서 확인하고자 하는 상태가 protected이다.
    - 해결방법 : 테스트 전용 하위클래스 패턴(Test Specific Subclass Pattern)
    - 의도 : SUT가 클래스에 테스트를 위한 기능을 제공하고 있지 않을 때,
             SUT의 하위 클래스를 만들어서 테스트되지 않은 요구사항을 검증할 수 있다.
    - 장점 : 제품코드를 변경하지 않고 테스트를 수행할 수 있다.

    이것이 테스트 전용인 하위 자식 클래스를 만드는 방법이다.

*/

#if 0

class TestUser : public User{
    public:
        int GetAge() const{
            return User::GetAge();
        }
};

#endif


class TestUser : public User{

    public:
        // 부모가 제공하는 메소드의 접근 지정자를 protected에서 public으로 변경할 수 있다.
        using User::GetAge; // 부모의 접근지정자를 자식에서 public으로 바꾸는 행위이다.

};








