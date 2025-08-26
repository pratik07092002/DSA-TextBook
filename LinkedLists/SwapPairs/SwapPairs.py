class nodeElement:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: nodeElement) -> nodeElement:
    dummy = nodeElement(-1)
    dummy.next = head
    prev = dummy

    while head and head.next:
        first = head
        second = head.next

        # swap
        prev.next = second
        first.next = second.next
        second.next = first

        # move pointers
        prev = first
        head = first.next

    return dummy.next
