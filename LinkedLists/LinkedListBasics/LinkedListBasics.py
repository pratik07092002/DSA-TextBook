class NodeElement:
    def __init__(self,data):
        self.data = data 
        self.next = None

head = NodeElement(10)
second = NodeElement(20)
third = NodeElement(30)   

head.next = second
second.next = third
third.next = None

temp = head  
while temp is not None:
    print("-> ", temp.data)
    temp = temp.next 

def array_to_LinkedList(arr):
    if not arr:
        return
    
    head = NodeElement(arr[0])
    current = head

    for i in range(1,len(arr)):
        current.next = NodeElement(arr[i])
        current = current.next

    return head

arr = [10, 20, 30, 40, 50]
def print_LL(head: NodeElement):
    temp = head 
    while temp is not None:
        print("Temp data ", temp.data)
        temp = temp.next

head = array_to_LinkedList(arr)

print_LL(head)