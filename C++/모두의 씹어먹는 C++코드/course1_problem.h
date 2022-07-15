/*
여러분은 아래와 같은 Date 클래스를 디자인 하려고 합니다. 
SetDate 는 말그대로 Date 함수 내부를 초기화 하는 것이고 
AddDay, AddMonth, AddYear 는 일, 월, 년을 원하는 만큼 더하게 됩니다. 
한 가지 주의할 점은 만일 2012 년 2 월 28 일에 3 일을 더하면 
2012 년 2 월 31 일이 되는 것이 아니라 2012 년 3 월 2 일이 되겠지요? (난이도 : 上)

class Date {
  int year_;
  int month_;  // 1 부터 12 까지.
  int day_;    // 1 부터 31 까지.

 public:
  void SetDate(int year, int month, int date);
  void AddDay(int inc);
  void AddMonth(int inc);
  void AddYear(int inc);

  void ShowDate();
};

*/
#include <iostream>

class course1_problem {
  int year_;
  int month_;  // 1 부터 12 까지.
  int day_;    // 1 부터 31 까지.

 public:
  course1_problem();
  
  void SetDate(int year, int month, int date);
  void AddDay(int inc);
  void AddMonth(int inc);
  void AddYear(int inc);

  void ShowDate();

};




