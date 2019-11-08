# Chaining

# reference: https://zuhern.github.io/2019-02-25-hash-table/

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable():
    def __init__(self, size = 9):
        self.table = [[] for i in range(0, size)]
        self.size = size

    def set(self, key, value):
        new_node = Node(key, value)

        box, item, in_index = self.find(key)

        if item == None:
            box.append(new_node)
        else:
            item = new_node

    def get(self, key):
        item, in_index = self.find(key)

        if item == None:
            return None
        
        return item.value

    def delete(self, key):
        box, item, in_index = self.find(key)

        if item == None:
            return False
        
        del_item = box.pop(in_index)
        return del_item.value
    
    def find(self, key):
        hash_key = hash(key)
        index = hash_key % self.size

        box = self.table[index]

        box_len = len(box)
        
        for in_index in range(0, box_len):
            item = box[in_index]

            if item.key == key:
                return box, item, in_index
        
        return box, None, -1

if __name__ == "__main__":
    hashtable = HashTable()

    def hash_set(key, value):
        return hashtable.set(1, 10)

    def hash_get(key):
        return hashtable.get(key)

    def hash_delete(key):
        return hashtable.delete(key)