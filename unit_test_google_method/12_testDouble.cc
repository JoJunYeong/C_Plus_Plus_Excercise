

#include  <string>


class FileSystem{
    public:
        bool IsValidFilename(const std::string& filename){
            // 현재의 파일 시스템에서 지원 가능한 파일 이름의 형태인지 확인한다.
            return true;
        }
};


class Logger{
    public:
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
            FileSystem fs;
            return fs.IsValidFilename(filename);

        }



};


#include <gtest/gtest.h>

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

