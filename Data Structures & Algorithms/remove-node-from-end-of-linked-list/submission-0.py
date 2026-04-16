# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0
        temp = head
        while temp:
            c +=1
            temp = temp.next
        
        c = c - n
        i = 0
        temp = head
        if c == 0: #edgecase #1: remove header node
            head = head.next
            return head if head else None
        while temp:
            if c == i + 1:
                temp.next = temp.next.next 
                break
            else:
                i += 1
                temp = temp.next
        
        return head


        