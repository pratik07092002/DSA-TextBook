# day 27 , 24-08-2025 
class ListNodeElement:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add2Numbers(l1:ListNodeElement , l2 : ListNodeElement)-> ListNodeElement :
    dummy = ListNodeElement()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0 
        
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        current.next = ListNodeElement(digit)
        current = current.next
        if l1: l1 =  l1.next
        if l2: l2 = l2.next 

    return dummy.next



# Helper to create linked list from Python list
def build_linked_list(values):
    dummy = ListNodeElement()
    current = dummy
    for v in values:
        current.next = ListNodeElement(v)
        current = current.next
    return dummy.next

# Helper to convert linked list to Python list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


l1 = build_linked_list([2,4,3])  
l2 = build_linked_list([5,6,4])   

res = add2Numbers(l1, l2)     
print(linked_list_to_list(res)) 
