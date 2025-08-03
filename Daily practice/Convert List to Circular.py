def make_circular(head):
    if not head: return None
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = head
    return head
