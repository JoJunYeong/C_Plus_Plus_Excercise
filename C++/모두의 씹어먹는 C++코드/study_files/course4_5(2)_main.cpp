#include "course4_5(2).hpp"

int main() {

  MyString str1("very very very long string");
  str1.reserve(30);

  std::cout << "Capacity : " << str1.capacity() << std::endl;
  std::cout << "String length : " << str1.length() << std::endl;
  str1.println();

  return 0;
}




