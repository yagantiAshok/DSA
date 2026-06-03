



class Node:

    def __init__(self,data):

        self.data = data
        self.ref = None


def take_input():

    value = int(input("Enter Number : -  "))

    head = None

    next = None

    while (value!=-1):

        newnode = Node(value)

        if (head==None):

            head = newnode

            next = newnode
        
        next.ref = newnode

        next = newnode
        
        
        # else:

        #     temp = head

        #     while (temp.ref!=None):

        #         temp = temp.ref
            
        #     temp.ref = newnode

        value = int(input("Enter Number : - "))
    
    return head

head = take_input()

# def insert_at_head(head,data):

#     new_node = Node(data)

#     new_node.ref = head

#     return new_node

# new_head = insert_at_head(head,8)

def insert_at_tail(head,data):

    newnode = Node(data)

    if (head is None):

        return newnode
    
    temp = head

    while (temp.ref!=None):

        temp = temp.ref 
    
    temp.ref = newnode

    return head

head = insert_at_tail(head,0)



def print_list(head):

    
    temp = head 

    while temp!=None:

        print(temp.data,end="->")

        temp = temp.ref
        

print_list(head)

