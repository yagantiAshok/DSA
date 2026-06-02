



class Node:

    def __init__(self,data):

        self.data = data
        self.ref = None

    
first = Node(10)

second = Node(11)

third = Node(12)

first.ref = second
second.ref = third



def print_list(head):

    
    temp = head 

    while temp!=None:

        print(temp.data,end="->")

        temp = temp.ref

# node(first)


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




print_list(head=head)

        
