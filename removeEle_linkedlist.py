#Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
#Return: 1 --> 2 --> 1 --> 4 --> 5, val = 1 output: 2,4,5


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        h = ListNode(0)
        h.next = head
        head = h
        while h.next:
            if h.next.val == val:
                h.next = h.next.next
            else:
                h = h.next
        return head.next 