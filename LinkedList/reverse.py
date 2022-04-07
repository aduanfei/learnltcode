class ListNode(object):
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode, terminal:ListNode):
        cur = head
        pre = None
        while cur != terminal:
            # 留下联系方式
            next = cur.next
            # 修改指针
            cur.next = pre

            # 继续往下走
            pre = cur
            cur = next
         # 反转后的新的头尾节点返回出去
        return tail, head

#递归前序
def dfs(head, pre):
    if not head: return pre
    next = head.next
    # # 主逻辑（改变指针）在后面
    head.next = pre
    dfs(next, head)

#dfs(head, None)

#递归后序
def dfs(head):
    if not head or not head.next: return head
    res = dfs(head.next)
    # 主逻辑（改变指针）在进入后面的节点的后面，也就是递归返回的过程会执行到
    head.next.next = head
    head.next = None

    return res