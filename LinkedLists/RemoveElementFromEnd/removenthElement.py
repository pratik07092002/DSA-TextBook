# day 28 , 25-08-2025 
class ListNodeElement:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head: ListNodeElement, n: int) -> ListNodeElement:
        # Dummy node to handle a case where n will be at 0th node
    dummy = ListNodeElement(0, head)
    primary = secondry = dummy

    # Step 1: Move fast ahead by n steps
    for _ in range(n):
        primary = primary.next

    # Step 2: Move fast until the end, moving slow as well
    while primary.next:
        primary = primary.next
        secondry = secondry.next

    # Step 3: Remove the node
    secondry.next = secondry.next.next

    return dummy.next