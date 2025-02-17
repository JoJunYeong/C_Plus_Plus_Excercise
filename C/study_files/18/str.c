#include "str.h"

char compare(char *str1, char *str2){

    while(*str1){
        if(*str1 != *str2)
            return 0;
        
        str1++;
        str2++;
    }

    if(*str2 == '\0') 
        return 1;
    else 
        return 0;
}

char copy_str(char *dest, char *src) {
  while (*src) {
    *dest = *src;
    src++;
    dest++;
  }

  *dest = '\0';

  return 1;
}