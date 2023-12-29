#  Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = final_list = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                final_list.next = list1
                list1 = list1.next
            else:
                final_list.next = list2
                list2 = list2.next
            final_list = final_list.next
        if list1:
            final_list.next = list1
        elif list2:
            final_list.next = list2

        return dum.next
