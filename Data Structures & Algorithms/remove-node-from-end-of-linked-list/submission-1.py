# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        temp = head
        while temp != None:
            nodes.append(temp)
            temp = temp.next
        if n == 0:
            nodes[len(nodes) - 2].next = None
            return head
        if n == len(nodes):
            head = head.next
            return head
        nodes[len(nodes) - n - 1].next = nodes[len(nodes) - n].next
        return head
        