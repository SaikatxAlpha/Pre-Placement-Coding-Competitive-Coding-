def insert_begin(head, val):
    node = Node(val)
    node.next = head
    return node
