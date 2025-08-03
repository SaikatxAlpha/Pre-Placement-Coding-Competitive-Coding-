def rotate(head, k):
    if not head: return head
    old_tail, n = head, 1
    while old_tail.next:
        old_tail = old_tail.next
        n += 1
    old_tail.next = head
    k = k % n
    new_tail = head
    for _ in range(n - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head
