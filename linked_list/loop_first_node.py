
'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the ref pointer. Internally, pos is used to denote the index of the node that tail's ref pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 
'''

from insert_opeartions import Node,take_input,print_list

head = take_input()

print_list(head)

def detect_cycle_first_node(head):

    
    slow = head
    fast = head

    while (fast is not None and fast.ref is not None):

        slow = slow.ref
        fast = fast.ref.ref

        if slow == fast:

            break
    else:

        return None
    
    fast = head

    while (fast!=slow):

        fast = fast.ref
        slow = slow.ref
    
    return fast 

head = detect_cycle_first_node(head)

print_list(head)