# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        ptr = head
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        arr.sort()
        size = len(arr)
        def instantiate(index):
            if index >= size:
                return None
            new_node = ListNode(arr[index],None)
            new_node.next = instantiate(index + 1)
            head = new_node
            return head
        return instantiate(0)