# day 25 , 22-08-2025

class ListNodeElement:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: ListNodeElement, headB: ListNodeElement) -> ListNodeElement:
    if not headA or not headB:
        return None

    pA, pB = headA, headB
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA   
