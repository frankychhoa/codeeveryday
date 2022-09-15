class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        d = head
        while d.next != None:
            if d.val == d.next.val:
                d.next = d.next.next
            else:
                d = d.next
        return head