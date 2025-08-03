def insert_end(head, val):
    node = Node(val)
    if not head:
        return node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = node
    return head
