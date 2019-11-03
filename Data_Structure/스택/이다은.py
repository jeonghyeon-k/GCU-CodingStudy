# 선입후출(FILO)
# Linked List 형식으로 구현(node)

# reference: https://velog.io/@imacoolgirlyo/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-3-Stack%EC%8A%A4%ED%83%9D

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if not self.head:
            return True
        else:
            return False
    
    def push(self, data):
        new_node = Node(data)

        # new_node의 next를 현재 head로 대입 후 같은 값을 가리키게 한다.
        # 현재 head를 new_node로 지정하여 new_node로 head 값 변경
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        
        pop_data = self.head.data
        self.head = self.head.next
        return pop_data

    def peek(self):
        if self.is_empty():
            return None
        
        return self.head.data

if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print("Peek data: {}".format(stack.peek()))

    if not stack.is_empty():
        for i in range(0, 2):
            print("Pop data: {}".format(stack.pop()))

    print("Peek data: {}".format(stack.peek()))