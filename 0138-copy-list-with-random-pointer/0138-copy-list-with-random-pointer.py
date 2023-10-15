"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#41
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None
        
        nodes = []
        randoms = []
        
        cur = head
        while cur:
            node = Node(cur.val)
            if len(nodes) > 0:
                nodes[-1].next = node
            
            nodes.append(node)
            
            if cur.random is None:
                randoms.append(None)
            else:
                rand = head
                randIndex = 0
                while rand != cur.random:
                    rand = rand.next
                    randIndex += 1
                randoms.append(randIndex)
            cur = cur.next
        
        for i,random in enumerate(randoms):
            if random is None:
                continue
            nodes[i].random = nodes[random]
            
        return nodes[0]
        
        
        