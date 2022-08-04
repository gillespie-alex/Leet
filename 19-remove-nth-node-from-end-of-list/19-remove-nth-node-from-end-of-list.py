# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # have one pointer that finds the length of the list
        length = 1
        ptr = head
        while ptr.next:
            ptr = ptr.next
            length += 1
        
        # now create a second traverse pointer to find the node and set its previous.next ptr
        trav = head
        if n == length:
            return head.next
        cnt = 0
        while cnt != length - n - 1:
            trav = trav.next
            cnt += 1
        temp = trav.next.next
        trav.next = temp
        return head
        