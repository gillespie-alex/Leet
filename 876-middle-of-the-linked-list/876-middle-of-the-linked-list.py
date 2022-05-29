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
        counter = 0
        fast, slow = head, head
        while (fast.next):
            fast = fast.next
            counter += 1
            if (counter % 2 == 0):
                slow = slow.next
        if counter % 2 != 0:
            #this means its odd and return the second middle node
            slow = slow.next
        return slow
        