#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = headB if not p1 else p1.next
            p2 = headA if not p2 else p2.next
        return p1

intersection_node = ListNode(123123123)
headA = ListNode(3)        
headA.next = ListNode(4)        
headA.next.next = ListNode(5)    
headA.next.next.next = intersection_node
headA.next.next.next.next = ListNode(6)


headB = ListNode(3)        
headB.next = ListNode(4)        
headB.next.next = intersection_node    
headB.next.next.next = ListNode(6)
headB.next.next.next.next = ListNode(7)

s = Solution()
print(s.getIntersectionNode(headA, headB).val)