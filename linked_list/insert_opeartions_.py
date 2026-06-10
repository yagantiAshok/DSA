



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
        else:
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

def print_list(head):

    
    temp = head 

    while temp!=None:

        print(temp.data,end="->")


        temp = temp.ref

print_list(head)
print()

# def insert_at_head(head,data):

#     new_node = Node(data)

#     new_node.ref = head

#     return new_node

# new_head = insert_at_head(head,8)

# def insert_at_tail(head,data):

#     newnode = Node(data)

#     if (head is None):

#         return newnode
    
#     temp = head

#     while (temp.ref!=None):

#         temp = temp.ref 
    
#     temp.ref = newnode

#     return head

# head = insert_at_tail(head,0)


# def insert_at_index(head,index,data):

#     if index==0:

#         return insert_at_head(head,data)

#     temp = head

#     count = 1

#     while (temp!=None and count<index-1):

#         count+=1

#         temp = temp.ref

#     if temp is None:

#         print( "Index out of range ")

#         return head

    
#     newnode = Node(data)

#     newnode.ref = temp.ref

#     temp.ref = newnode

#     return head


# head = insert_at_index(head,3,0)



# def insert_at_index_recursively(head,index,data):

#     if (index == 0):

#         newnode = Node(data)

#         newnode.ref = head

#         return newnode
    
#     if (head is None):

#         print("Index out of range")

#         return head
    
#     head.ref = insert_at_index_recursively(head.ref,index-1,data)

#     return head 

# head = insert_at_index_recursively(head,4,100)


# deleting oprations

# def delete_head_node(head):

# #     if (head is None):

# #         return "no elements"
    
# #     new_head = head.ref

# #     return new_head
    
# # head = delete_head_node(head)

# # print(head)

# # def delete_tail_node(head):

# #     if (head is None) :# if (head is None or head.ref==None):

# #         return None
    
# #     if (head.ref==None):

# #         return delete_head_node(head)
    
# #     previous_node = head

# #     temp = head

# #     while temp.ref!=None:# temp.ref.ref

# #         previous_node  = temp

# #         temp = temp.ref
    
# #     previous_node.ref = temp.ref

# #     return head

# # head = delete_tail_node(head)

# # print(head)

# # def recursively_remove_tail(head):

# #     if (head is None or head.ref == None):

# #         return None
    
# #     head.ref = recursively_remove_tail(head.ref)

# #     return head


# # head = recursively_remove_tail(head)


# # def delete_at_index(head,index):

# #     if ( index==0 ):

# #         head = head.ref

# #         return head 
    
# #     if (head is None):

# #         return None
    
# #     count = 0
# #     temp = head

# #     while (temp!=None and count<index-1):

# #         temp = temp.ref

# #         count+=1

# #     if (temp is None or temp.ref==None):

# #         return "index out of range"
    
# #     tail_end = temp.ref

# #     temp.ref = tail_end.ref

# #     return head


# # head = delete_at_index(head,3)
# # def delete_node_recursively(head,index):

        
# #     if (head is None):

# #         print("index out of range or no element")

# #         return None

# #     if (index == 0 ):

# #         return head.ref

    
# #     head.ref = delete_node_recursively(head.ref, index - 1)

# #     return head

# # head = delete_node_recursively(head,0)

# # print(head)


# # def delete_node_by_value(head,value):


# #     if (head is None):

# #         print("No elements")

# #         return None
    

# #     if (head.data==value):

# #         return head.ref

# #     temp = head

# #     while (temp.ref!=None):

# #         if (temp.ref.data==value):

# #             temp.ref = temp.ref.ref

# #             return head
        
# #         temp = temp.ref
    
# #     print("That element not presented")

# #     return head


# # head = delete_node_by_value(head,value)
    

# def search_LL_BY_value(head,value):

#     if (head is None):

#         print("No linked list")

#         return None
    
#     temp = head

#     while (temp is not None):

#         if (temp.data == value):

#             return True
        
#         temp = temp.ref
        

#     return False

# print()

# value = int(input("Enter number to search : "))

# store = search_LL_BY_value(head,value)

# print(store)

# print()

# print("After deleted")

# print_list(head)


# def middle_of_linked_list(head):

#     low = head 

#     high = head 

#     while (high is not None):


#         if (high.ref is not None):
           
#             low = low.ref

#             high = high.ref.ref

#         else:
           
#            high = None


    
#     return low

# head = middle_of_linked_list(head=head)


# def print_list(head):

    
#     temp = head 

#     while temp!=None:

#         print(temp.data,end="->")


#         temp = temp.ref

# print_list(head)

first = Node(1)
second = Node(2)
third = Node(3)

head_true = first 
head_true.ref=second
second.ref = third
third.ref = first

del(first)
del(second)
del(third)

# print_list(head_true)







def fast_method(head):

    
    slow = head
    fast = head

    while (fast is not None and fast.ref is not None):

        slow = slow.ref

        fast = fast.ref.ref

        if slow==fast:

            return True
    
    return False

print(fast_method(head_true))