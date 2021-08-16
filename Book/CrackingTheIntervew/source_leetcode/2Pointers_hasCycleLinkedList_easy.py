#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True
                
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(3)
head.next.next.next.next = head.next.next

# expect, linkedlist has cycle
s = Solution()
print(s.hasCycle(head))
        