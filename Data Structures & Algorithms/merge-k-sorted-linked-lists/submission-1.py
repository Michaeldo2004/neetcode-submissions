# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        mergedHead = None
        currNode = None
        if not lists:
            return None

        for linklist in lists:
            if linklist:
                heapq.heappush(heap, (linklist.val, id(linklist), linklist))

        while heap:
            val, someid, head = heapq.heappop(heap)
            if not mergedHead:
                mergedHead = head
                currNode = mergedHead
            else:
                currNode.next = head
                currNode = currNode.next
            if head.next:
                heapq.heappush(heap, (head.next.val, someid, head.next))
        return mergedHead