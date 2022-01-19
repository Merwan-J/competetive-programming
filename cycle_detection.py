def has_cycle(head):
    arr = []
    while head:
        if head in arr:
            return 1
        arr.append(head)
        head = head.next
    return 0
