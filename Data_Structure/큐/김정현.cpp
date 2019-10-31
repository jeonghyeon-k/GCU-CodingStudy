#include <iostream>
using namespace std;

struct Node
{
friend struct Queue;

private:
    int data;
    Node *next;
public:
    Node(){
        next=NULL;
        data=0;
    }
};

struct Queue
{
private:
    Node * front;
    Node * rear;
    int size = 0;
public:
    Queue(){
        front=NULL;
        rear=NULL;
    }
    void enQueue(int i){
       Node*node = new Node();
       node->data=i;
       if(size==0){
           front=rear=node;
        }
       else{
           rear->next=node;
           rear=rear->next;
       }
       size++;
    }
    void deQueue(){
      if(size==0){return;}
      else{
          Node *tmp= front;
          front= tmp->next;
          size--;
      }
    }
    void print(){
       Node*tmp=front;
       while(tmp->next){
           cout<<tmp->data<<endl;
           tmp=tmp->next;
           if(tmp->next==NULL){
               cout<<tmp->data<<endl;
           }
       }
    }
    ~Queue(){}
};

int main(){
    Queue * queue = new Queue();
    queue->enQueue(1);
    queue->enQueue(2);
    queue->enQueue(3);
    queue->enQueue(4);
    queue->enQueue(5);
    queue->print();
    queue->deQueue();
    queue->deQueue();
    queue->print();

}


