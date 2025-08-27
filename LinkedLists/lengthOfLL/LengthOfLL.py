
class ListNodeElement:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def LengthOfLL(head: ListNodeElement )-> int:
    dummy = ListNodeElement(0)
    dummy.next = head
    current = dummy
    count = 0
    while current.next is not None:
        count = count + 1
        current = current.next

    return count 


def build_list(arr):
    dummy = ListNodeElement(0)
    current = dummy
    for num in arr:
        current.next = ListNodeElement(num)
        current = current.next
    return dummy.next


head = build_list([1,2,6,3,4,5,6])
answer = LengthOfLL(head)
print(answer)

