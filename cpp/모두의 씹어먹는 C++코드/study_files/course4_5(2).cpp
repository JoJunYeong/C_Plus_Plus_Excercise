#include "course4_5(2).hpp"

MyString::MyString(char c) {
  string_content = new char[1];
  string_content[0] = c;
}
MyString::MyString(const char* str) {
  string_length = strlen(str);
  string_content = new char[string_length];

  for (int i = 0; i != string_length; i++) {
    string_content[i] = str[i];
  }
}
MyString::MyString(const MyString& str) {
  string_length = str.string_length;
  string_content = new char[string_length];

  for (int i = 0; i != string_length; i++)
    string_content[i] = str.string_content[i];
}
MyString::~MyString() { delete[] string_content; }
int MyString::length() const { return string_length; }

void MyString::print() const {
  for (int i = 0; i != string_length; i++) {
    std::cout << string_content[i];
  }
}
void MyString::println() const {
  for (int i = 0; i != string_length; i++) {
    std::cout << string_content[i];
  }

  std::cout << std::endl;
}


MyString& MyString::assign(const MyString& str) {
  if (str.string_length > memory_capacity) {
    // 그러면 다시 할당을 해줘야만 한다.
    delete[] string_content;

    string_content = new char[str.string_length];
    memory_capacity = str.string_length;
  }
  for (int i = 0; i != str.string_length; i++) {
    string_content[i] = str.string_content[i];
  }

  // 그리고 굳이 str.string_length + 1 ~ string_length 부분은 초기화
  // 시킬 필요는 없다. 왜냐하면 거기 까지는 읽어들이지 않기 때문이다.

  string_length = str.string_length;

  return *this;
}


MyString& MyString::assign(const char* str) {
  int str_length = strlen(str);
  if (str_length > string_length) {
    // 그러면 다시 할당을 해줘야만 한다.
    delete[] string_content;

    string_content = new char[str_length];
    memory_capacity = str_length;
  }
  for (int i = 0; i != str_length; i++) {
    string_content[i] = str[i];
  }

  string_length = str_length;

  return *this;
}


int MyString::capacity() { 
    return memory_capacity; 
}

void MyString::reserve(int size) {
  if (size > memory_capacity) {
    char *prev_string_content = string_content;

    string_content = new char[size];
    memory_capacity = size;

    for (int i = 0; i != string_length; i++)
      string_content[i] = prev_string_content[i];

    delete[] prev_string_content;
  }

  // 만일 예약하려는 size 가 현재 capacity 보다 작다면
  // 아무것도 안해도 된다.
}

char MyString::at(int i) const {
  if (i >= string_length || i < 0)
    return NULL;
  else
    return string_content[i];
}





