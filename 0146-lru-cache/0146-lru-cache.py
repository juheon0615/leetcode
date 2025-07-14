class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.removeNode(self.map[key])
        self.appendToBack(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.removeNode(self.map[key])
        elif len(self.map) == self.capacity:            
            self.removeNode(self.map.pop(self.head.key))

        node = Node(key, value)
        self.map[key] = node
        self.appendToBack(node)


    def removeNode(self, node) -> Optional[Node]:
        if node is None:
            return None
        
        nextNode = node.next
        prevNode = node.prev

        if prevNode is not None:
            prevNode.next = nextNode
        
        if nextNode is not None:
            nextNode.prev = prevNode
        
        if node is self.tail:
            self.tail = prevNode

        if node is self.head:
            self.head = nextNode

        return node

    def appendToBack(self, node):
        node.next = None
        node.prev = None

        if self.tail is None:
            self.head = node
            self.tail = node
            return
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.tail.next = None    
    

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)