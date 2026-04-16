class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.diction = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cap = capacity
        self.size = 0

    def get(self, key: int) -> int:
        someNode = self.diction.get(key)
        if not someNode: return -1
        # take node out of cache
        someNode.prev.next = someNode.next
        someNode.next.prev = someNode.prev
        # move it to the front before dummy head
        someNode.prev = self.head
        someNode.next = self.head.next
        self.head.next.prev = someNode
        self.head.next = someNode

        return someNode.val

    def put(self, key: int, value: int) -> None:
        temp = Node(key, value)

        # if key exists ->
        # update node
        if key in self.diction.keys():
            #delete first node
            curr = self.diction[key]
            curr.next.prev = curr.prev
            curr.prev.next = curr.next
            self.diction[key] = temp
        else:
            self.diction[key] = temp
            self.size +=1 
        # add to top of cache
        temp.prev = self.head
        temp.next = self.head.next
        self.head.next.prev = temp
        self.head.next = temp
        # take out least used node
        if self.size > self.cap:
            curr = self.tail.prev
            curr.prev.next = self.tail
            self.tail.prev = curr.prev
            self.diction.pop(curr.key)
            self.size -=1




