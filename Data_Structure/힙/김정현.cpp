

#include <iostream>
using namespace std;

int number;
int heap[1000000];

void heapify(int i){

    // C = 왼쪽 노드
    int c = 2*i+1; 

    if(c<number && heap[c]<heap[c+1]){
        c++;
    }

    if(heap[i]<heap[c]){
        int temp = heap[i];
        heap[i]= heap[c];
        heap[c]=temp;
    }

    if(c<= number /2){
        heapify(c);
    }

}

int main(void){
    //힙 생성 숫자 입력
    cin >> number;

    //숫자만큼 데이터 받기
    for(int i = 0; i>number;i++){
        cin >> heap[i];
    }

    //힙 생성
    for(int i = number/2; i>=0; i--){
        heapify(i);
    }

    for(int i= number -1;i>-0;i--){
        for(int j = 0; j< number; j++){
            cout<< heap[i]<<"";
        }
        cout<<'\n';
        // 루트 변경
        int temp = heap[0];
        heap[0]=heap[i];
        heap[i]=temp;

        int root=0;
        int c=1;
        do{
            c = 2*root+1;
            if(c<i-1&&heap[c]<heap[c+1]) c++;
            if(c<i&& heap[root]<heap[c]){
                temp = heap[root];
                heap[root] = heap[c];
                heap[c] = temp;
            }
            root=c;

        }while(c<i);
    }
}