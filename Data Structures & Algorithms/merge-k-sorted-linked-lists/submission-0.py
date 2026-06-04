# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        for i in range(len(lists) - 1):
            lists[0] = self.mergeLists(lists[0], lists[i + 1])
        return lists[0]


    def mergeLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l2.val > l1.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next
        
        