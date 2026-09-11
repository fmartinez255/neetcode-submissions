# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.lists = lists
        return self.mergeSort(0, len(lists)-1)

    def mergeSort(self, start: int, end: int) -> Optional[ListNode]:
        if start > end:
            return None

        if start == end:
            return self.lists[start]

        middle = (start + end) // 2

        left = self.mergeSort(start, middle)
        right = self.mergeSort(middle+1, end)

        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next