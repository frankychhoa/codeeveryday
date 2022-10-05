class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ref=head
        pre=ListNode()
        current=head
        while ref.next != None:
            pre=ListNode()
            current=head
            
            if ref.next.val < ref.val:
                curRef=ListNode(ref.next.val)
                try:
                    ref.next=ref.next.next
                except:
                    ref.next=None

                while current != None:
                    if pre.next==None and curRef.val <= current.val:
                        curRef.next=current
                        head=curRef
                        break
                    elif pre.val <= curRef.val and curRef.val < current.val:
                        curRef.next=current
                        pre.next=curRef
                        break
                    pre=current
                    current=current.next
            else:
                ref=ref.next
        return head