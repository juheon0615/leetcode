# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        lenB = 0
        
        curA = headA 
        curB = headB

        while curA:
            curA = curA.next
            lenA += 1
        
        while curB:
            curB = curB.next
            lenB += 1
        
        curA = headA 
        curB = headB
        
        if lenA > lenB:
            while lenA > lenB:
                curA = curA.next
                lenA -= 1
        elif lenA < lenB:
            while lenA < lenB:
                curB = curB.next
                lenB -= 1        
        else:
            pass
        
        ret = None
        while curA and curB:
            if curA is curB:
                ret = curA
                break
            else:
                curA = curA.next
                curB = curB.next
                
        return ret
            
    

        