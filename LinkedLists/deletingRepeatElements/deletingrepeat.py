# day 24, 21-08-2025 

class NodeElement:
    def __init__(self , val = 0 , next = None):
        self.val = val 
        self.next = next

def deleteRepeatingElement(head: NodeElement):
    current = head
    while current and current.next:
        if(current.val == current.next.val):
            current.next = current.next.next
        else:
            current = current.next
    return head                     