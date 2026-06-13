




from insert_opeartions import Node,take_input


head = take_input()

def cycle_length(head):


    slow = head
    fast = head

    while (fast is not None and fast.ref is not None):

        slow = slow.ref
        fast = fast.ref.ref

        if fast==slow:

            break
    else:

        return 0
    
    count = 1

    fast = fast.ref

    while (fast!=slow):

        count+=1

        fast = fast.ref
    
    return count 


print(cycle_length(head))