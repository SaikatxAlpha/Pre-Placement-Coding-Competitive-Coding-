def sort_list(head):
    if not head or not head.next: return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    mid = slow.next
    slow.next = None
    l = sort_list(head)
    r = sort_list(mid)
    return merge(l, r)
