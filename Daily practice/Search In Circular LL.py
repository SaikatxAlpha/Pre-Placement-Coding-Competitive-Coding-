def search_cll(head, val):
    if not head: return False
    curr = head
    while True:
        if curr.val == val:
            return True
        curr = curr.next
        if curr == head:
            break
    return False
