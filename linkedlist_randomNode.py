# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        ans = cnt = 0
        head = self.head
        while head:
            if random.randint(0, cnt) == 0:
                ans = head.val
            head, cnt = head.next, cnt + 1
        return ans