
// assign 함수

#include <iostream>
#include <string.h>

class MyString {
    
  char* string_content;  // 문자열 데이터를 가리키는 포인터
  int string_length;     // 문자열 길이
  int memory_capacity;  // 할당된 메모리 크기

 public:
  // 문자 하나로 생성
  MyString(char c);

  // 문자열로 부터 생성
  MyString(const char* str);

  // 복사 생성자
  MyString(const MyString& str);

  ~MyString();

    MyString& assign(const MyString& str);
    MyString& assign(const char* str);

    int capacity() ;
    void reserve(int size) ;

  int length() const;

  void print() const;
  void println() const;
  char at(int i) const;
};









