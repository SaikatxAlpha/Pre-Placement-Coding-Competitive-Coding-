def delete_val(head, val):
    dummy = Node(0)
    dummy.next = head
    prev, curr = dummy, head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next
