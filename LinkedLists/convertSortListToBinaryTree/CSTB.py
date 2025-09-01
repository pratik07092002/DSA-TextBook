# day 34 , 1-09-2025

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head: ListNode) -> TreeNode:
    if not head:
        return None
    if not head.next:   
        return TreeNode(head.val)
    prev = None
    slow, fast = head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if prev:
        prev.next = None

    root = TreeNode(slow.val)

    root.left = sortedListToBST(head if slow != head else None)
    root.right = sortedListToBST(slow.next)

    return root
