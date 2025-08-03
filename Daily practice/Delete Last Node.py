def delete_last(head):
    if not head or not head.next:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head
