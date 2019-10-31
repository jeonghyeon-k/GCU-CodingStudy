#include <iostream>
#include <algorithm>
using namespace std;


int main(void){
    int number;
    int data[1000000];

    cin >> number;
    for(int i=0;i<number; i++){
        cin>> data[i];
    }
    sort(data, data+number);
    for(int i=0;i<number;i++){
        cout<<data[i];
    }
    return 0;
    
}
