# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.h = head
        self.palindrome = True
        self.reverse_through(head)
        return self.palindrome

    def reverse_through(self, head):
        if head != None:
            self.reverse_through(head.next)
            if head.val == self.h.val:
                self.h = self.h.next
            else:
                self.palindrome = False
        else:
            return