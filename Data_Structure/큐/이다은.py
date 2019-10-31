# 선입선출(FIFO)
# Linked List 형식으로 구현(node)

# reference: https://wayhome25.github.io/cs/2017/04/18/cs-21/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if not self.head:
            return True
        else:
            return False

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node
    
    def dequeue(self):
        if self.is_empty():
            return None

        get_data = self.head.data
        self.head = self.head.next
        return get_data

    def peek(self):
        if self.is_empty():
            return None
        
        return self.head.data

if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)

    print("Dequeue data: {}".format(queue.dequeue()))
    print("Peek data: {}".format(queue.peek()))

    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    for i in range(0, 3):
        print("Dequeue data: {}".format(queue.dequeue()))

    print("Peek data: {}".format(queue.peek()))