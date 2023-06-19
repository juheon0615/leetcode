# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nodes = set()
        
        cur = head
        ret = None
        while cur:
            if cur in nodes:
                ret = cur
                break
            else:
                nodes.add(cur)
                cur = cur.next
        
        return ret
        
        