class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next
def insert_last(head, tail, data):
    newNode = Node(data)
    if head:
        tail.next = newNode
        tail = newNode
    else:
        head = tail = newNode
    return head, tail
def print_list(head):
    if head:
        while head.next:
            print(head.data, end=' ')
            head = head.next
        print(head.data)
    else:
        print("Empty list")
def union(head1, head2):
    union_set = set()
    while head1:
        union_set.add(head1.data)
        head1 = head1.next
    while head2:
        union_set.add(head2.data)
        head2 = head2.next
    union_set = list(union_set)
    union_set.sort()

    head = tail = None
    for ele in union_set:
        head, tail = insert_last(head, tail, ele)

    return head
def intersection(head1, head2):
    list1_set = set()
    while head1:
        list1_set.add(head1.data)
        head1 = head1.next

    intersection_set = set()
    while head2:
        if head2.data in list1_set:
            intersection_set.add(head2.data)
        head2 = head2.next

    intersection_set = list(intersection_set)
    intersection_set.sort()

    head = tail = None
    for ele in intersection_set:
        head, tail = insert_last(head, tail, ele)

    return head

if __name__ == '__main__':
    lst1_len, lst2_len = [int(ele) for ele in input().split()]
    # lst1_len, lst2_len = [int(ele) for ele in "4 4".split()]

    lst1 = [int(ele) for ele in input().split()]
    # lst1 = [int(ele) for ele in "10 15 4 20".split()]
    lst2 = [int(ele) for ele in input().split()]
    # lst2 = [int(ele) for ele in "8 4 2 10".split()]

    head1 = tail1 = None
    head2 = tail2 = None

    for i in range(lst1_len):
        head1, tail1 = insert_last(head1, tail1, lst1[i])

    for i in range(lst2_len):
        head2, tail2 = insert_last(head2, tail2, lst2[i])

    union_list = union(head1, head2)
    intersection_list = intersection(head1, head2)

    print_list(union_list)
    print_list(intersection_list)