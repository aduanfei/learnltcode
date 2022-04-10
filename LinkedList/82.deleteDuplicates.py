
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head
        pre = prehead = ListNode(-99981, head)
        cur = curdup = head
        while (cur != None):
            while (curdup and curdup.val == cur.val):
                curdup = curdup.next
            if curdup == cur.next:
                pre = cur
                cur = cur.next

            else:
                pre.next = curdup
                cur = curdup

        return prehead.next