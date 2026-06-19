

"""
stack using Built in List

"""

class StackUsingList:

    def __init__(self):
        
        self.__stack = []
    
    def push(self,data):

        self.__stack.append(data)

        print(f"{data} is pushed into stack")
    
    def is_empty(self):

        if (len(self.__stack)==0):

            return True
        
        return False  # return len(self.__stack)==0
    
    def top(self):

        if (self.is_empty()):

            print("stack has no elements, empty")

            return None
        
        return self.__stack[-1]
    
    def size(self):

        return len((self.__stack))
    
    def pop(self):

        if (self.is_empty()):

            print("stack is empty, we can't use pop")

            return None
        
        return self.__stack.pop()
        

        

mystack = StackUsingList()

print(mystack.is_empty())
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)
print(mystack.top())
print(mystack.pop())
print(mystack.top())
print(mystack.pop())

print(mystack._StackUsingList__stack)