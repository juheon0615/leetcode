# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        lCur = None
        gCur = None
        
        lHead = None
        gHead = None
        
        cur = head
        while cur:
            n = cur.next
            if cur.val >= x:
                if gHead is None:
                    gCur = cur
                    gHead = cur
                else:
                    gCur.next = cur
                    gCur = gCur.next
            else:
                if lHead is None:
                    lCur = cur
                    lHead = cur
                else:
                    lCur.next = cur
                    lCur = cur
            cur.next = None
            cur = n
        
        
        if lHead:
            lCur = lHead

            while lCur.next:
                lCur = lCur.next

            lCur.next = gHead
        
        return lHead if lHead else gHead
    
        
        
        
        