/*  fseek ?��?�� ?��?��  */

#include <stdio.h>

int main(){

    FILE *fp = fopen("some_data.txt","r");
    char data[10];
    char c;

    if(fp == NULL){
        printf("File Open Error! \n");
        return 0;
    }

    fgets(data, 5, fp);
    printf("�Է� ���� ������  : %s \n", data);

    c = fgetc(fp);
    printf("�� ������ �Է� ���� ���� : %c \n", c);

    fseek(fp, -1, SEEK_CUR);

    c = fgetc(fp);
    printf("�׷��ٸ� ���� ���ڰ�? : %c\n", c);

    fclose(fp);


    return 0;
}





