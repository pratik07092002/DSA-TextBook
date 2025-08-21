
# # Day 23, 20-08-2025
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
# Tried Again on Day 24 after completing basics of Linked List
class NodeElement:
    def __init__(self,data):
        self.data = data 
        self.next = None 
def merge_Sorted_List(list1H:NodeElement , list2H: NodeElement)-> NodeElement:
    dummy = NodeElement(-1)
    current = dummy


    while list1H and list2H:
        if(list1H.data < list2H.data):
            current.next = list1H
            list1H = list1H.next
        else:
            current.next = list2H
            list2H = list2H.next
        current = current.next

    if list1H:
        current.next = list1H
    if list2H:
        current.next = list2H

    return dummy.next


def createLinkedListAndReturnHead(arr):
    if not arr:
        return
    head = NodeElement(arr[0])
    temp = head
    
    for i in range(1,len(arr)):
        temp.next = NodeElement(arr[i])
        temp = temp.next
    return head
def printLL(nodehead:NodeElement):
    temp = nodehead
    while temp is not None:
        print("Merged List is ", temp.data)
        temp = temp.next 

l1h = createLinkedListAndReturnHead([1,2,3,4,5])
l2h = createLinkedListAndReturnHead([1,2,3,4,5,8,9])

mergerdListHead = merge_Sorted_List(l1h,l2h) 
printLL(mergerdListHead)



