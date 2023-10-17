# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = {}
        cur = head
        
        while cur:
            if cur.val not in vals:
                vals[cur.val] = 1
            else:
                vals[cur.val] += 1
            cur = cur.next
        
        ret = None
        cur = head
        prev = None
        while cur:
            if vals[cur.val] > 1:
                if prev: 
                    prev.next = cur.next
            else:
                if ret is None:
                    ret = cur
                prev = cur
            cur = cur.next
        
        return ret
        