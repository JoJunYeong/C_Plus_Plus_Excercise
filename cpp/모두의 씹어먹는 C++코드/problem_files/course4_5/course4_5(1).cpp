#include "course4_5(1).hpp"

String::String(char c){

    // mStrLen = 1;
    // if(mStr)
    //     delete[] mStr;
    // mStr = new char[2];
    // strcpy(mStr,(char *)c);

}

String::String(char *c){

    if(mStr)
        delete[] mStr;
    int i = 0;
    while(1){
        if(c[i]=='\0'){  
            mStrLen = i;          
            break;
        }
        i++;
    }
    mStr = new char[mStrLen];
    strcpy(mStr,c);

}

String::~String(){
    if(mStr)
        delete[] mStr;
}

int String::StringLenth(String s){

    return s.mStrLen;

}  // 문자열 길이를 구하는 함수

void String::AddString(String s){

    char *tmp = new char[mStrLen+s.mStrLen-1];
    strcpy(tmp,mStr);
    strcat(tmp,s.mStr);
    delete[] mStr;
    mStr = new char[mStrLen+s.mStrLen-1];
    strcpy(mStr,tmp);
    std::cout << mStr << std::endl;
}   // 문자열 뒤에 다른 문자열 붙이기

bool String::IsStringInside(String s){

    if(mStrLen < s.mStrLen)
        return false;

    for(int j = 0 ; j < mStrLen-s.mStrLen+1 ; j++){
        for(int i =0 ; i< s.mStrLen ; i++){
            if(mStr[i] != s.mStr[i]){
                return false;
                break;
            }
        }
    }
    return true;

}  // 문자열 내에 포함되어 있는 문자열 구하기

bool String::IsSame(String s){

    if(mStrLen == s.mStrLen){
        for(int i =0 ; i< mStrLen ; i++){
            if(mStr[i] != s.mStr[i]){
                return false;
                break;
            }
        }
        return true;
    }
    else{
        return false;
    }
}  // 문자열이 같은지 비교

bool String::IsFrontOfDictinary(String s){

    if(mStrLen >= s.mStrLen){
        for(int i =0 ; i< s.mStrLen ; i++){
            if(mStr[i] > s.mStr[i]){
                return false;
                break;
            }
            else if(mStr[i] < s.mStr[i]){
                return true;
                break;
            }
        }
    }
    else{
        for(int i =0 ; i< mStrLen ; i++){
            if(mStr[i] > s.mStr[i]){
                return false;
                break;
            }
            else if(mStr[i] < s.mStr[i]){
                return true;
                break;
            }
        }
    }
    return false;
} // 문자열 크기 비교 






