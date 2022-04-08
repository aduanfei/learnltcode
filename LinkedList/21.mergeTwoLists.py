class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1==None:
            return list2
        elif list2==None:
            return list1
        if list1.val>list2.val:
            h1=list2
            h2=list1
        else:
            h1=list1
            h2=list2
        head=h1
        while(h2!=None):
            while(h1.next!=None and h2.val>=h1.next.val ):
                h1=h1.next
            temp1=h1.next
            temp2=h2.next
            h1.next=h2
            h2.next=temp1
            h2=temp2
            h1=h1.next
        return head