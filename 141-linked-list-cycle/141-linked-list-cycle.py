# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # node_map = {0:0}
        # if not head: return False
        # while head.next:
        #     node_map[head.val] = 1 + node_map.get(head.val, 0)
        #     #node_map[head.val] = 1 if not node_map[head.val] else node_map[head.val] += 1
        #     if node_map[head.val] > 1: 
        #         print(node_map)
        #         return True
        #     head = head.next
        # return False
        
        node_map = {0:0}
        if not head: return False
        while head.next:
            if head in node_map.keys(): return True
            node_map[head] = 1
            head = head.next
        return False
        