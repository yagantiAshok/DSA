



from insert_opeartions import Node , take_input

head = take_input()

def checking_linkedlist_palindrome(head):

    if  (head is  None ):
        return False


    slow = head

    fast = head

    while (fast is not None and fast.ref is not None):

        slow = slow.ref
        fast = fast.ref.ref

    # reverse second part

    prev = None

    curr = slow

    while curr is not None:

        next  = curr.ref

        curr.ref = prev

        prev = curr

        curr  = next
    
    while (prev is not None):

        if (prev.data==head.data):

            prev = prev.ref

            head = head.ref
        
        else:

            return False
    
    return True

print(checking_linkedlist_palindrome(head))



