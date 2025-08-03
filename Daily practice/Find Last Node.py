def last_node(head):
    while head and head.next:
        head = head.next
    return head
