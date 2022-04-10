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
        #每次反转后的末尾节点
        linknode = ListNode(0)
        ish1 = False

        #循环至末尾
        while (count > 1):

            count = count - 1
            cur = cur.next
            if cur == None:
                break

            #计数k次
            if count == 1:
                #先保存下一节点
                tempnext=cur.next
                #返回反转后的头尾
                h1, h2 = self.reversek(head, k)
                linknode.next = h1
                linknode = h2
                if not ish1:
                    #保存反转链表头
                    res = h1
                    ish1 = True
                count = k
                cur = tempnext
                head=cur
                #cur可能为空
                if cur == None:
                    break
        #最后链接未反转链表
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