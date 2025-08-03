def second_last(head):
    if not head or not head.next: return None
    while head.next.next:
        head = head.next
    return head
