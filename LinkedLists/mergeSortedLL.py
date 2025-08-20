
# Day 23, 20-08-2025
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    current = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    return dummy.next


def build_linked_list(values):
    dummy = ListNode(-1)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

list1 = build_linked_list([1,2,3,3,5])
list2 = build_linked_list([1,2,2,2,0])

merged_head = mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_head))
