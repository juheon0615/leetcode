# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse(node):
            if node is None:
                return ""
            else:
                return reverse(node.next) + " " + str(node.val)
        
        def inorder(node):
            if node is None:
                return ""
            else:
                return str(node.val) + " " + inorder(node.next)
        
        
        cur1 = head
        cur2 = head
        
        str1 = reverse(cur1)
        str2 = inorder(cur2)
        
        str1 = str1.strip()
        str2 = str2.strip()
        
        print(str1)
        print(str2)
        return True if str1 == str2 else False
        
            
        
        
        