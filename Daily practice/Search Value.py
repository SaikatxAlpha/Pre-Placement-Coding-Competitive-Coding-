def search(head, val):
    while head:
        if head.val == val:
            return True
        head = head.next
    return False
