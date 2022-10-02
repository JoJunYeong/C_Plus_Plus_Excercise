/*
문제 1
Date 클래스에 여러가지 생성자들을 추가해보세요 (난이도 : 下)


*/

#include <iostream>

class Date {
  int year_;
  int month_;  // 1 부터 12 까지.
  int day_;    // 1 부터 31 까지.

 public:
  void ShowDate();

  Date() {
    std::cout << "기본 생성자 호출!" << std::endl;
    year_ = 2012;
    month_ = 7;
    day_ = 12;
  }

  Date(int year, int month, int day) {
    std::cout << "인자 3 개인 생성자 호출!" << std::endl;
    year_ = year;
    month_ = month;
    day_ = day;
  }

    Date(int year) {
    std::cout << "인자 1 개인 생성자 호출!" << std::endl;
    year_ = year;
  }


};

void Date::ShowDate() {
  std::cout << "오늘은 " << year_ << " 년 " << month_ << " 월 " << day_
            << " 일 입니다 " << std::endl;
}
int main() {
  Date day = Date();
  Date day2(2012, 10, 31);
  Date day3(2016);

  day.ShowDate();
  day2.ShowDate();
  day3.ShowDate();

  return 0;
}






