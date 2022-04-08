# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = k
        linknode = ListNode(0)
        ish1 = False
        while (count > 1):

            count = count - 1
            cur = cur.next
            if cur == None:
                break
            if count == 1:
                tempnext=cur.next
                h1, h2 = self.reversek(head, k)
                linknode.next = h1
                linknode = h2
                if not ish1:
                    res = h1
                    ish1 = True
                count = k
                cur = tempnext
                head=cur
                if cur == None:
                    break
            linknode.next=head
        return res

    def reversek(self, head, k):
        orghead = head
        next = head.next
        head.next = None
        while (k > 1):
            temp = next.next
            next.next = head
            head = next
            next = temp
            k = k - 1
        return head, orghead

ls=[1,2]
head=ListNode(1)
cur=head
for i in range(1,len(ls)):
    cur.next=ListNode(ls[i])
    cur=cur.next

s1=Solution()
res=s1.reverseKGroup(head,2)
while(res):
    print(res.val)
    res=res.next