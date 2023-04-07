#include <gtest/gtest.h>

int foo() {return 42;}
int goo() {return 100;}

/*
1. ASSERT_
-   단언문이 실패할 경우, 이후의 코드를 수행하지 않는다.
    하나의 테스트 케이스 안에 여러개의 단언문이 존재할 경우
    이후의 단언문이 수행되지 않는 문제가 있다.
    "죽은 단언문"
    > 하나의 테스트 케이스 안에 여러개의 단언문을 두지말자고 xUnit Test Pattern에서는 정의함.
        그러나 이렇게 처리하면 중복된 테스트 케이스가 발생하고, 유지보수 비용이 증가한다는 단점이 있다.
    
    > Google Test는 새로운 단언문을 제공한다.
        EXPECT_EQ / NE / LT / GT / LE / GE / TRUE / FALSE .....

*/



// 기존 xUnitTest방식의 ASSERT_EQ
TEST(SampleTest, Sample1){
    //검증
    ASSERT_EQ(42,foo());
    ASSERT_EQ(100,goo());
    ASSERT_EQ(42,foo());
    ASSERT_EQ(100,goo());

}

// Google방식의 EXPECT_EQ
// 단언문이 실패하면 테스트의 결과는 실패이고, 이후의 검증을 계속한다.
TEST(SampleTest, Sample2){
    //검증
    EXPECT_EQ(42,foo());
    EXPECT_EQ(100,goo());
    EXPECT_EQ(42,foo());
    EXPECT_EQ(100,goo());

}

// 1. 사전조건 단언문
class User {
    std::string name = "Tom";
    int age = 42;


    public:
        std::string GetName() const {return name;}
        int GetAge() const {return age;} 
};

User* GetUser() {return new User;}
// User* GetUser() {return nullptr;}

TEST(UserTest, Sample3){
    User* user = GetUser(); // user를 불러왔는데,
    ASSERT_NE(user,nullptr);    // user 가 null이 아니어야 해 NE = Negative
    // 이렇게 하면 user가 null이 아닐때만 밑에를 실행하게 된다.
    // 이를 사전조건 단언문이라 한다.
    // 이렇듯 무조건 EXPECT만 써도 안된다.

    EXPECT_EQ(user->GetName(), "Tom");
    EXPECT_EQ(user->GetAge(), 42);
}


// 2. 문자열 비교 단언문
/*
    => const char* / char[] 형태의 문자열 비교에서 사용해야 합니다.
        - EXPECT_STREQ / EXPECT_STRNE
        - EXPECT_STRCASEEQ / EXPECT_STRCASENE : 대소문자 무시
*/

TEST(SampleTest2, Sample1){
    std::string s1 = "hello";
    std::string s2 = "hello";
    EXPECT_EQ(s1,s2);

    char s3[] = "HELLO";
    const char* s4 = "hello";
    EXPECT_EQ(s3, s4);
    EXPECT_STREQ(s3, s4);
    EXPECT_STRCASEEQ(s3,s4);
}

// 3. 부동소수점 비교 단언문
// - float, double
// EXPECT_FLOAT_EQ(Equal) / EXPECT_DOUBLE_EQ(Equal)

// - 오차 범위를 직접 지정하고 싶다.
// EXPECT_NEAR
TEST(SampleTest3, Sample1){
    double a = 0.7;
    double b = 0.1 * 7;

    // EXPECT_EQ(a,b);
    // EXPECT_DOUBLE_EQ(a,b);
    EXPECT_NEAR(a,b,0.00000001);    //!!
    // EXPECT_EQ(a,b);
}



// 4. 예외 검증을 위한 단언문
// => EXPECT_THROW : 기대한 예외가 발생하는지 여부를 검즘
//    EXPECT_ANY_THROW : 예외 발생 여부를 검즘
//    EXPECT_NO_THROW : 예외가 발생하지 않음을 검증
void OpenFile(const std::string filename){
    if(filename.empty()) {
        throw std::invalid_argument("invalid filename");
    }
    // ...
}

TEST(SampleTest4, Sample2){
    std::string invalidFilename = "";
    EXPECT_THROW(OpenFile(invalidFilename), std::invalid_argument);
    // EXPECT_ANY_THROW(OpenFile(invalidFilename));
    // EXPECT_NO_THROW(OpenFile(invalidFilename));
}






/*
    잘못된 파일 이름이 인자로 전달되었을 경우, invalid_argument예외가
    발생하는지 여부를 검증하고 싶다.
*/
TEST(SampleTest4, Sample1){
    try{
        std::string invalidFilename = "";
        OpenFile(invalidFilename);
        FAIL() << "예외가 발생하지 않음.";
    }catch (std::invalid_argument&){
        SUCCEED();
    }catch(...){
        FAIL() << "기대한 예외와 다른 예외가 발생하였음.";
    };
}





/*
    5. 테스트 비활성화
    내가 TEST 를 만들었는데, 이게 수정/작성중일때.
    누군가 이 작성중인 테스트를 비활성화 하기 위해 주석처리를 하면, "잊혀진 테스트"가 된다.
    => 그래서 테스트의 결과에 포함되진 않지만, 비활성화된 테스트가 존재한다는 사실을 알려야 한다.
    => 구글은 이를 위한 조치를 해놓았다.
    => TestSuite이름 또는 TestCase의 이름이 DISABLED_ 접두를 가지면 비활성화 된다.
    => 비활성화 된 테스트를 구동하는 옵션이 존재한다.
        $ ./a.out --gtest_also_run_disabled_tests
*/
TEST(DISABLED_SampleTest5, Sample1){
    FAIL() <<"작성중입니다.";
    // 문제는 이게 수정/작성중인데, 이게 실패함으로 인해서 다른게 문제가 생길 수 있다.
}

TEST(SampleTest5, DISABLED_Sample2){
    FAIL() <<"작성중입니다.";
    // 문제는 이게 수정/작성중인데, 이게 실패함으로 인해서 다른게 문제가 생길 수 있다.
}


// 클래스를 비활성화 하면 명시적 TEST의 경우 모두 TEST이름도 바꿔주어야 한다.
class DISABLED_ImageTest : public testing::Test {};
TEST_F(DISABLED_ImageTest, BlurImage) { }
TEST_F(DISABLED_ImageTest, ResizeImage) { }




