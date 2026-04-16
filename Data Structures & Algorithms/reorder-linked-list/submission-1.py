# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        half = slow.next # half -> end
        slow.next = None 

        prevhalf = None
        while half:
            temp = half.next
            half.next = prevhalf
            prevhalf = half
            half = temp
        

        first = head

        while first and prevhalf:
            temp = first.next
            temp2 = prevhalf.next

            first.next = prevhalf
            prevhalf.next = temp
            
            first = temp
            prevhalf = temp2


            

        