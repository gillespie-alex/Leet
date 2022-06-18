# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return 
        heap =[]
        for i in range(len(lists)):
            if not lists[i]: continue
            head = lists[i]
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        # create linked list of all the values in heap
        res = []
        while heap:
            node = ListNode(heapq.heappop(heap))
            res.append(node)
        if not res: return
        
        # now initialize all the next pointers
        head = res[0]
        temp = head
        for i,nodes in enumerate(res):
            if i == len(res) - 1:
                break;
            temp.next = res[i+1]
            temp = temp.next
        return head