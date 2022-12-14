def merge(h1, h2):
    if h1.data < h2.data:
        h = t = h1
        h1 = h1.bottom
    else:
        h = t = h2
        h2 = h2.bottom
    while h1 and h2:
        if h1.data <= h2.data:
            t.bottom = h1
            t = t.bottom
            h1 = h1.bottom
        else:
            t.bottom = h2
            t = t.bottom
            h2 = h2.bottom
    if h1:
        t.bottom = h1
    else:
        t.bottom = h2

    return h

def flatten(root):
    if root:
        while root and root.next:
            r = merge(root, root.next)
            if r != root:
                root = root.next
            else:
                root.next = root.next.next
    return root
