# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ret = None
        cur = head
        
        cnt = 0
        begin = None
        prev = None
        if k == 1:
            return head
        while cur:
            cnt += 1
            if cnt == 1:
                begin = cur
                cur = cur.next
            elif cnt == k:
                revCur = begin
                revPrev = None
                
                curNext = cur.next
                while revCur is not curNext:
                    tmp = revCur.next
                    revCur.next = revPrev
                    revPrev = revCur
                    revCur = tmp
                
                if prev:
                    prev.next = cur
                else:
                    ret = cur
                    
                begin.next = curNext
                prev = begin
                cnt = 0
                cur = curNext
            else:
                cur = cur.next
                

            
        
        
        
        return ret
        
        