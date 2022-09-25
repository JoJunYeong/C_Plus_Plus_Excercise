// ����ü

#include <stdio.h>

char copy_str(char *dest, const char *scr);

struct Books {  // 구조체의 정의에서는 변수를 초기화 할 수 없다.
   /* 책 이름 */
  char name[30];
  /* 저자 이름 */
  char auth[30];
  /* 출판사 이름 */
  char pub[30];
  /* 빌려 졌나요? */
  int borrowed;
};

// int main() {
//   struct Books Harry_Potter;

//   copy_str(Harry_Potter.name, "Harry Potter");
//   copy_str(Harry_Potter.auth, "J.K. Rolling");
//   copy_str(Harry_Potter.pub, "Scholastic");
//   Harry_Potter.borrowed = 0;

//   printf("책 이름 : %s \n", Harry_Potter.name);
//   printf("저자 이름 : %s \n", Harry_Potter.auth);
//   printf("출판사 이름 : %s \n", Harry_Potter.pub);

//   return 0;
// }

int main() {

  struct Books book_list[3];
  int i;

  for(i=0;i<3;i++){
    printf("책 %d 정보 입력 : ",i);
    scanf("%s%s%s",book_list[i].name, book_list[i].auth, book_list[i].pub);
    book_list[i].borrowed = 0;
  }

  for(i=0;i<3;i++){
    printf("-------------------------- \n");
    printf("책 %s 의 정보\n", book_list[i].name);
    printf("저자 : %s \n",book_list[i].auth);
    printf("출판사 : %s \n",book_list[i].pub);

    if(book_list[i].borrowed == 0)
      printf("안 빌려짐\n");
    else 
      printf("빌려짐\n");

  }

  return 0;
}





char copy_str(char *dest, const char *src) {
  while (*src) {
    *dest = *src;
    src++;
    dest++;
  }

  *dest = '\0';

  return 1;
}








