# Remove Linked List Elements
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        tem1=ListNode()
        tem1.next=head
        temp=tem1
        while temp.next:
            if temp.next.val == val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return tem1.next
