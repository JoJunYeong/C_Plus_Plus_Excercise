



/*
    아래래와 같이 Logger를 표현했을 때, 문제가 생긴다. 바로 그것은 
    우리는 Logger에서 설정한 
    if(name.size() < 5){
                return false;
            }
    이것이 조건에 맞는지 안맞는지를 알아보아야 하는데, 

                // 현재의 파일 시스템에서 가능한 이름인지 확인이 필요하다.
            FileSystem fs;
            return fs.IsValidFilename(filename);
    
    이 부분이 테스트의 결과에 영향을 주기 때문이다.
    그래서 우리는 우리가 테스트하고자 하는 부분만 확인하기 위해 
    TestDouble이라는 테스트 대역을 사용해야한다.
    쉽게 보자면, 저 위의 FileSystem 변수인 fs는 무조건 true를 반환하게 하는 것이다.

    즉 testdouble의 목적은 다음과 같다.
    목적 : 테스트 환경을 통제하기 위해서 사용한다.

    => 테스트 대역은 무조건 적용이 불가능하다.
        제품의 코드가 테스트 대역을 적용할 수 잇는 형태의 설계여야 가능하다.
        "약한결합 / 느슨한 결합"

        강한결합 : 협력 객체를 이용할 때, 구체적인 타입에 의존한다.
        약한결합 : 협력 객체를 이용할 때, 구체적인 타입이 아니라, 추상타입(추상클래스, 인터페이스)에 의존한다. 

    그래서 이를 가능하게 하기 위해 여기에서는 테스트의 과정에서 무조건 true를 반환해야 하는 
    FileSystem에 대한 인터페이스인 IFileSystem를 만들어서 대응한다.


*/



#include  <string>

class IFileSystem{
    public:
        virtual ~IFileSystem() { }
        virtual bool IsValidFilename(const std::string& filename) = 0;
};

class FileSystem : public IFileSystem {
    public:
        bool IsValidFilename(const std::string& filename){
            // 현재의 파일 시스템에서 지원 가능한 파일 이름의 형태인지 확인한다.
            return false;
        }
};


// 이전 문제 코드
// class FileSystem{
//     public:
//         bool IsValidFilename(const std::string& filename){
//             // 현재의 파일 시스템에서 지원 가능한 파일 이름의 형태인지 확인한다.
//             return true;
//         }
// };


class Logger{
    IFileSystem* fs;

    public:
        Logger(IFileSystem* p = nullptr)
            : fs(p)
            {
                // 기존 제품코드가 사용하던 방식과 동일하게 사용할 수 있도록 해준다.
                if(fs == nullptr) {
                    fs = new FileSystem;
                }
            }


        /*
            확장자를 제외한 파일의 이름이 5글자 이상이어야 한다.
            예)
            file.log => file => invaild
            hello.log => hello => vaild
        */
        bool IsValidLogFilename(const std::string& filename){
            size_t index = filename.find_last_of(".");
            std::string name = filename.substr(0,index);
            if(name.size() < 5){
                return false;
            }

            // 현재의 파일 시스템에서 가능한 이름인지 확인이 필요하다.
            // FileSystem fs;

            /*
                2) 협력 객체를 직접 생성하는 것이 아니라, 외부에서 생성해서 전달해야 한다.
                IFileSystem* fs = new FileSystem;
                => 의존성 주입(Dependency Injection)
                    1) 생성자 주입
                        : 협력 객체가 필수적일 때
                    2) 메소드 주입
                        : 협력 객체가 필수적이지 않을 때

            */

            return fs->IsValidFilename(filename);

        }



};


#include <gtest/gtest.h>

// 테스트 대역을 만드는 방법
// => 일반적으로 협력 객체의 인터페이스를 구현합니다.

class TestDouble : public IFileSystem {
    public:
        // 무조건 성공합니다.
        bool IsValidFilename(const std::string& filename){
            return true;
        }
};



TEST(LoggerTest, IsValidLogFilename_NameLonggerThan5Chars_ReturnsTrue){
    Logger logger;
    std::string validFilename = "valid.log";

    EXPECT_TRUE(logger.IsValidLogFilename(validFilename))
        << "확장자를 제외한 파일명이 다섯글자 이상일 때.";
}

TEST(LoggerTest, IsValidLogFilename_NameLonggerThan5Chars_Returnsfalse){
    Logger logger;
    std::string invaildFilename = "badyyyy.log";

    EXPECT_FALSE(logger.IsValidLogFilename(invaildFilename))
        << "확장자를 제외한 파일명이 다섯글자 미만일 때.";

}

