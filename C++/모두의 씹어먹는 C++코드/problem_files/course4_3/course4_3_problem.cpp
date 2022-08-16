#include "course4_3_problem.hpp"

string::string(char c, int n){

    mStr = new char[n+1];
    for(int i = 0 ; i < n ; i++)
        mStr[i] = c;
    mLen = n;
}

string::string(const char *s){

    mStr = (char*)s;
    int i=0;
    while(1){
        if(mStr[i] == NULL){
            mLen = i+1;
            break;
        }
        i++;
    }
}

string::string(const string &s){

    mStr = s.mStr;
    mLen = s.strlen();
}

string::~string(){

    if(mStr) 
        delete[] mStr;

}



void string::add_string(const string &s){

    mLen = strlen() + s.strlen();
    char * tmp = new char[strlen() + s.strlen() -1 ];
    strcpy(tmp,mStr);
    strcat(tmp,s.mStr);
    delete[] mStr;
    mStr = new char[mLen+1];
    strcpy(mStr,tmp);
    delete[] tmp;

}


void string::copy_string(const string &s){

    if(mStr)
        delete[] mStr;
    mStr = new char[s.strlen() ];
    strcpy(mStr,s.mStr);

}


int string::strlen() const{

    if(mStr)
        return mLen;
    else
        return 0;
    
}
