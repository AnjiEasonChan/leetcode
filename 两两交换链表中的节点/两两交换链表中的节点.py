# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head and head.next:
            head.next.next, head.next, head = head, self.swapPairs(head.next.next), head.next
        return head
