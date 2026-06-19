

"""
stack using Built in List

"""

# class StackUsingList:

#     def __init__(self):
        
#         self.__stack = []
    
#     def push(self,data):

#         self.__stack.append(data)

#         print(f"{data} is pushed into stack")
    
#     def is_empty(self):

#         if (len(self.__stack)==0):

#             return True
        
#         return False  # return len(self.__stack)==0
    
#     def top(self):

#         if (self.is_empty()):

#             print("stack has no elements, empty")

#             return None
        
#         return self.__stack[-1]
    
#     def size(self):

#         return len((self.__stack))
    
#     def pop(self):

#         if (self.is_empty()):

#             print("stack is empty, we can't use pop")

#             return None
        
#         return self.__stack.pop()
        

        

# mystack = StackUsingList()

# print(mystack.is_empty())
# mystack.push(10)
# mystack.push(20)
# mystack.push(30)
# mystack.push(40)
# print(mystack.top())
# print(mystack.pop())
# print(mystack.top())
# print(mystack.pop())

# print(mystack._StackUsingList__stack)


"""
stack using linked list 

"""


class Node:

    def __init__(self,val):
        
        self.data = val
        self.next = None

class StackUsingLL:

    def __init__(self):
        
        self.head = None

        self.size = 0
    
    def push(self,data):

        newnode = Node(data)

        newnode.next = self.head

        self.head = newnode

        self.size+=1
    
    def is_empty(self):

        if self.size==0:

            return True
        
        return False
    
    def peek(self):

        if not (self.is_empty()):

            return self.head.data
        
        return None
    
    def pop(self):

        if not (self.is_empty()):

            popped_data = self.head.data

            self.head = self.head.next

            self.size-=1

            return popped_data
        
        return None
    

    def __len__(self):

        return self.size
    
mystack  = StackUsingLL()


            

print(mystack.is_empty())
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)
print(mystack.peek())
print(mystack.pop())
print(mystack.peek())
print(mystack.pop())
print(len(mystack))

    
