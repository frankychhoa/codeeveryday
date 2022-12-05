# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=1
        nextHead=head
        while True:
            if not nextHead.next:
                break
            count += 1
            nextHead = nextHead.next
        #print(count)
        m=1
        res=head
        while True:
            if m == (count//2+1):
                break
            m += 1
            res = res.next
        return res