def remove_zero_sum(head):
    dummy = Node(0)
    dummy.next = head
    curr = dummy
    prefix = 0
    seen = {}
    while curr:
        prefix += curr.val
        seen[prefix] = curr
        curr = curr.next
    curr = dummy
    prefix = 0
    while curr:
        prefix += curr.val
        curr.next = seen[prefix].next
        curr = curr.next
    return dummy.next
