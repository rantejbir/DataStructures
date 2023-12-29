# adding two numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy = ListNode(0)
        current = dummy
        # return l1 if l1 is None else l2
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum=val1+val2+carry
            digit=sum%10
            carry=sum//10
            current.next=ListNode(digit)
            current=current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
