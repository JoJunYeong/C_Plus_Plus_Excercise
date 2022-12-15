#include <stdio.h>


int main(){

    FILE *fp;
    fp = fopen("some_data.txt","r");
    char data[10];
    char c;

    if(fp == NULL){
        printf("file open error ! \n");
        return 0;
    }

    fseek(fp,-1,SEEK_END);
    c= fgetc(fp);
    printf("The end of char on the file is %c\n",c);

    fclose(fp);


    return 0;
}