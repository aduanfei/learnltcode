
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or k==0:
           return head
        numn=0
        p=head
        tl=p
        while(p!=None):
            numn+=1
            tl=p
            p=p.next
        kn=numn-(k%numn)

        if kn==0:
            return head
        else:
            kn=kn-1
        cur=head
        pre=None
        while(kn>0):
            kn=kn-1
            pre=cur
            cur=cur.next
        tl.next=head
        head=cur.next
        cur.next=None
        return head