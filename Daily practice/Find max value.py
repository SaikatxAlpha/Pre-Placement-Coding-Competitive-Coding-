def max_node(head):
    if not head: return None
    m = head.val
    while head:
        m = max(m, head.val)
        head = head.next
    return m
