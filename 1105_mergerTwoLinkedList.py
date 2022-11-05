# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        ##decide head
        head = ListNode()
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        res = head
        def mergeRecur(head,list1,list2):

            if list1 and not list2:
                head.next = list1
                list1 = None
            elif not list1 and list2:
                head.next = list2
                list2 = None
            elif list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
                mergeRecur(head.next,list1,list2)
            else:
                head.next = list2
                list2 = list2.next
                mergeRecur(head.next,list1,list2)
        mergeRecur(head,list1,list2)
        return res