# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sHead = None
        uHead = head

        while uHead is not None:
            
            new = uHead
            uHead = uHead.next 
            new.next = None

            if sHead is None:
                sHead = new
            else:
                prev = None
                sCur = sHead
                
                while sCur is not None:
                    if new.val <= sCur.val:
                        if prev is None:
                            tmp = sHead 
                            sHead = new
                            sHead.next = tmp
                        else:
                            prev.next = new
                            new.next = sCur
                        break
                    else:
                        if sCur.next is None:
                            sCur.next = new
                            break
                        else:
                            prev = sCur
                            sCur = sCur.next
                
            
        return sHead
        
        
        
            
        
        