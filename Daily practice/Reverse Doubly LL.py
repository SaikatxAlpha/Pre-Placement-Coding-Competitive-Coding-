def reverse_dll(head):
    curr = head
    while curr:
        curr.prev, curr.next = curr.next, curr.prev
        if not curr.prev:
            return curr
        curr = curr.prev
