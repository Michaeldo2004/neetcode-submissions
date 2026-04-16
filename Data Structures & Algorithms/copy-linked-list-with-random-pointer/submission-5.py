"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {} # input node : new node with val only
        curr = head
        if not head: return None
        while curr:
            newNode = Node(curr.val)
            copy[curr] = newNode
            curr = curr.next
        
        curr = head
        while curr:
            newNode = copy[curr]
            
            newNode.next = copy[curr.next] if curr.next else None
            newNode.random = copy[curr.random] if curr.random else None

            curr = curr.next
        
        return copy[head]
        