def length(head):
    c = 0
    while head:
        c += 1
        head = head.next
    return c
