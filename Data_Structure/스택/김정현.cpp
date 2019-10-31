#include <iostream>
using namespace std;

struct Node
{
friend struct Stack;

private:
    int data;
    Node *next;
public:
    Node(){
        next=NULL;
        data=0;
    }
    Node(int i, Node *ptr){
        data=i;
        next=ptr->next;
        ptr->next=this;
    }
};
struct Stack
{
private:
    Node *head;
    int count;
public:
    Stack(){
        head= new Node();
        count=0;
    }
     

    void pop(){
        Node*tmp=head;
        head = head->next;
        delete tmp;
        count--;
    }

    void push(int i){
        new Node(i,head);
        count ++;
    }
    void print(){
        Node*tmp = head;
        while(tmp->next){
            tmp=tmp->next;
            cout<< tmp->data <<endl;
        }
    }
    ~Stack(){}
};
int main(){
    Stack *stack = new Stack();
    stack->push(1);
    stack->push(2);
    stack->push(3);
    stack->print();
    stack->pop();
    stack->print();
}


