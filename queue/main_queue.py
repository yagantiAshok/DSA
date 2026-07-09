



# class Queue:

#     def __init__(self):
        
#         self.__queue = []
    
#     def enqueue(self,data):

#         self.__queue.append(data)
    
#     def is_empty(self):

#         return len(self.__queue)==0
    
#     def dequeue(self):

#         if self.is_empty():

#             return None
        
#         return self.__queue.pop(0)
    
#     def __len__(self):
        
#         return len(self.__queue)
    
#     def front(self):

#         if self.is_empty():

#             return None
        
#         return self.__queue[0]

        

# queue = Queue()

# print(queue.is_empty())

# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)

# print(queue.front())
# print(queue.dequeue())
# print(queue.front())
# print(queue.dequeue())
# print(queue.front())

# print(len(queue))

# # print(queue.__queue)

class Node:

    def __init__(self,data):
        
        self.data = data
        self.ref = None



class QueueUsingLL:

    def __init__(self):
        
        self.__head = None
        self.__tail = None
        self.__size = 0

    def enqueue(self,data):

        newnode = Node(data)
        self.__size +=1
        if self.__head == None:
            self.__head = newnode
            self.__tail = newnode
        else:
            self.__tail.ref = newnode
            self.__tail  = newnode
    
    def is_empty(self):

        return self.__size==0
    
    def dequeue(self):

        if self.is_empty():
            return None
        
        self.__size-=1
        first_element = self.__head.data
        self.__head = self.__head.ref
        return first_element
    
    def front(self):

        if self.is_empty():
            return None

        return self.__head.data
    
    def __len__(self):
        
        return self.__size

queue = QueueUsingLL()



    
print(queue.is_empty())#true

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(len(queue))

print(queue.front())#10
print(queue.dequeue())#10
print(queue.front())#20
print(queue.dequeue())#20
print(queue.front())#30
print(queue.dequeue())#30
print(queue.front())#None

print(queue.is_empty())#true

print(len(queue))   
