# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = None
        
        cur1 = list1
        cur2 = list2
        
        while cur1 and cur2:
            nextNode = None
            if cur1.val > cur2.val:
                nextNode = cur2
                cur2 = cur2.next
            else:
                nextNode = cur1
                cur1 = cur1.next
            
            if head is None:
                head = cur = nextNode
            else:
                cur.next = nextNode
                cur = cur.next
        
        if cur1 is not None:
            if head is None:
                head = cur1
            else:
                cur.next = cur1
        elif cur2 is not None:
            if head is None:
                head = cur2
            else:
                cur.next = cur2        

        
        
        return head
        