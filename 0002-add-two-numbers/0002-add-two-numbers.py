# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur =  None
        carry = False
        while l1 or l2:
            v1 = v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            curSum = v1 + v2
            if carry:
                curSum += 1

            if curSum > 9:
                carry = True
                curSum = curSum % 10
            else:
                carry = False
            
            # print("v1: %d v2: %d curSum: %d" % (v1,v2,curSum))
            # print("carry: ", carry)
            if head is None:
                head = ListNode(curSum)
                cur = head
            else:
                cur.next = ListNode(curSum)
                cur = cur.next
        if carry:
            cur.next = ListNode(1)
        return head

        