# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        if k % len(ist) == 0 no change
        
        '''
        
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        if k == 0 or n == 0:
            return head
        
        k = k % n
        if k == 0:
            return head
        s = n - k
        e = n - k - 1
        
        newStart = head
        newEnd = head
        curEnd = head
        
        for _ in range(s):
            newStart = newStart.next
        
        for _ in range(e):
            newEnd = newEnd.next
        
        while curEnd.next:
            curEnd = curEnd.next
            
        curEnd.next = head
        newEnd.next = None
        
        return newStart
        
        
        
        