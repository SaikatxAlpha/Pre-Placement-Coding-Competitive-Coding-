def create_list(vals):
    head = Node(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head
