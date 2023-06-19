# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node, prev):
            if node.next is None:
                return node
            else:
                temp = node.next
                node.next = prev
                return reverse(temp, node)
        
        
        
        cur = head
        prev = None
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        ret = prev
        return ret
        
        