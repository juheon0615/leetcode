# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        nodes = [] 
        head = None
        
        for l in lists:
            if l is not None:
                cur = l
                while cur:
                    nodes.append(cur)
                    cur = cur.next
        
        
        nodes.sort(key=lambda x:x.val)
        
        for i in range(len(nodes)):
            if i == len(nodes) - 1:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i+1]
                                
        
        if len(nodes) > 0:
            head = nodes[0]
        
        return head
                
                