
#include <iostream>

using namespace std;

struct img {
    int mas[256][256];
};


int middlepoint (int t, int s, int d) {
    float mx=0;
    float my=0;
    
    if (d==0){
        cout <<"Яркость всех точек ниже порога";
    }
    else {
        mx=t/d;
        my=s/d;
        cout << "среднее значение координат по икс "<< mx<<", а по игрек "<< my;
    }
};


void init(img& image) {
    for (int i=0;i<255;i++){
        for (int j=0;j<255;j++){
            image.mas[i][j]=7;
        }
    }
}
    

int main(){
    int k;
    int counter;
    int xadd=0;
    int yadd=0;
    img PICTURE;
    
    cout<<"введите порог яркости ";
    cin >>k; 
    
    init(PICTURE);
    
    for (int i=0;i<255;i++) {
        for (int j=0;j<255;j++) {
            if (PICTURE.mas[i][j]>k) {
                counter++;
                xadd=xadd+i;
                yadd=yadd+j;
            }
        }
    }
    
    middlepoint(xadd,yadd,counter);
}

