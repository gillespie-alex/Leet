# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next == 0:
            return head
        fast = ListNode(head)
        fast.next = head.next
        i = 0
        while (fast.next is not None):
            i += 1
            if i % 2 == 0:
                head = head.next
            fast = fast.next
        #at this point we've reached the end of the list
        
        if i%2 is not 0:
            return head.next
        else:
            return head
            
        