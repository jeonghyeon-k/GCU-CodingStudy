# a kind of Sort
# Time Complexity: O(log n)

# reference: https://daimhada.tistory.com/108

class MaxHeap:
    def __init__(self):
        self.queue = []

    def parent(self, index):
        return (index-1) // 2

    def leftchild(self, index):
        return 2*index + 1
    
    def rightchild(self, index):
        return 2*index + 2

    def swap(self, i, parent_index):
        tmp = self.queue[i]
        self.queue[i] = self.queue[parent_index]
        self.queue[parent_index] = tmp
    
    def maxHeapify(self, i):
        left_index = self.leftchild(i)
        right_index = self.rightchild(i)
        max_index = i

        if left_index <= len(self.queue)-1 and self.queue[max_index] < self.queue[left_index]:
            max_index = left_index
        if right_index <= len(self.queue)-1 and self.queue[max_index] < self.queue[right_index]:
            max_index = right_index

        if max_index != i:
            self.swap(i, max_index)
            self.maxHeapify(max_index)

    def insert(self, n):
        self.queue.append(n)
        last_index = len(self.queue)-1

        # 아래에서 위로 올라가면서 부모와 자식간의 비교
        while 0 <= last_index:
            parent_index = self.parent(last_index)
            if 0 <= parent_index and self.queue[parent_index] < self.queue[last_index]:
                self.swap(last_index, parent_index)
                last_index = parent_index
            else:
                break
    
    def delete(self):
        last_index = len(self.queue)-1

        if last_index < 0:
            return -1
        
        self.swap(0, last_index)
        maxValue = self.queue.pop()

        # root에서부터 재정렬
        self.maxHeapify(0)

        print(maxValue)
        return maxValue
    
    def printHeap(self):
        print(self.queue)

if __name__ == "__main__":
    maxheap = MaxHeap()

    maxheap.insert(2)
    maxheap.insert(5)
    maxheap.insert(14)
    maxheap.insert(1)
    maxheap.insert(8)
    maxheap.printHeap()
    maxheap.delete()
    maxheap.printHeap()
    maxheap.delete()
    maxheap.insert(23)
    maxheap.insert(6)
    maxheap.printHeap()
    maxheap.delete()
    maxheap.printHeap()
    maxheap.delete()