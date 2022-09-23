#include<stdio.h>

int main(){


    char str_a[] = "abc";
    char str_b[] = "abc";

    for(int i= 0; i< 3 ; i++){
        if(str_a[i]!=str_b[i]){
            printf("\n0\n");
            return 0;
        }
        if(i==2){
            printf("\n1\n");
            return 1;
        }
    }

    return 0;
}