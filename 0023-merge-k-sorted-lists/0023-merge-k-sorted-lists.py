# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    class Entry:
        def __init__(self, val, node):
            self.val = val
            self.node = node

        def __lt__(self, other):
            return self.val < other.val

        def __repr__(self):
            return f"PriorityTask({self.val})"
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        heapq.heapify(heap)
        
        
        for l in lists:
            cur = l
            while cur:
                heapq.heappush(heap, Solution.Entry(cur.val, cur))
                cur = cur.next
        
        
        prev = head = None

        while len(heap) > 0:
            cur = heapq.heappop(heap)
            if head is None:
                head = cur
            else:
                prev.next = cur
            
            prev = cur
        
        if prev is not None:
            prev.next = None

        return head