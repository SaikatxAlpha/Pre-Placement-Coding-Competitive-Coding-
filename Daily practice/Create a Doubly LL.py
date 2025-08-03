class DNode:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

def create_dlist(vals):
    head = DNode(vals[0])
    curr = head
    for v in vals[1:]:
        node = DNode(v)
        node.prev = curr
        curr.next = node
        curr = node
    return head
