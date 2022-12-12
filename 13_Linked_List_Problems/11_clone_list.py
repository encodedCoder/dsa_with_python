"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head:
        # STEP-1: Create a simple hashmap for given list
            my_dict_1 = dict()
            temp = head; i = 1
            while temp:
                my_dict_1[temp] = (i, temp.random)
                temp = temp.next
                i += 1

        # STEP-2: Simply create the copy of linked_list
            temp_head = head
            new_head  = temp = Node(temp_head.val)

            while temp_head.next:
                temp_head = temp_head.next

                new_node  = Node(temp_head.val)
                temp.next = new_node
                temp = temp.next

        # STEP-3: Create hashmap for copied list
            my_dict_2 = dict()
            temp = new_head; i = 1
            while temp: 
                my_dict_2[i] = temp
                temp = temp.next
                i += 1

        # STEP-4: Fix the random pointers
            t1 = head; t2 = new_head
            while t1:
                if t1.random != None:
                    random_node_address = my_dict_1[t1][1]
                    random_node_number  = my_dict_1[random_node_address][0]
                    # print(random_node_number)
                    t2.random = my_dict_2[random_node_number]
                else:
                    t2.random = None
                t1 = t1.next
                t2 = t2.next

        # FINAL STEP: Resturn the new_list_head
            return new_head