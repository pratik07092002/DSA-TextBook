class ListNodeElement:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElement(head: ListNodeElement , val: int)-> ListNodeElement:
    dummy = ListNodeElement(0)
    dummy.next = head
    current = dummy

    while current.next is not None:
        if(current.next.val == val):
            current.next = current.next.next
        else:
            current = current.next
    return dummy.next


def build_list(arr):
    dummy = ListNodeElement(0)
    current = dummy
    for num in arr:
        current.next = ListNodeElement(num)
        current = current.next
    return dummy.next

# Helper function to print linked list
def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


head = build_list([1,2,6,3,4,5,6])
new_head = removeElement(head, 6)
print(print_list(new_head))  

