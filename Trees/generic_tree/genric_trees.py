

# def fun():
#     for i in range(0):
#         print(i)
# print(fun())

from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
    
# root = TreeNode(1)
# child1=TreeNode(2)
# child2=TreeNode(3)
# child3=TreeNode(4)

# root.children.append(child1)
# root.children.append(child2)
# root.children.append(child3)

# child1.children.append(child3)


# for child_object in root.children:
#     print(child_object.data)
# for child_object in root.children:
#     print(child_object.children)

# def print_data(root):

#     print(root.data)
#     for child in root.children:
#         print_data(child)
# print_data(root)

def print_children_detailed(root):

    if (root==None):
        return 
    print(root.data,end=":")
    for child in root.children:
        print(child.data,end=",") # print(*[child.data for child in root.children],sep=",",end="")
    print()
    for child in root.children:
        print_children_detailed(child)

# print_children_detailed(root)

# def take_input():

#     data = int(input("Enter Data For The Node : "))
#     node = TreeNode(data)
#     children = int(input(f"Enter No of Childrens for {data} :  "))
#     for _ in range(children):
#         child = take_input()
#         node.children.append(child)
#     return node
# root = take_input()

# print_children_detailed(root)

def take_input_level_wise():
    
    data = int(input("Enter data for Root Node : "))
    root = TreeNode(data)
    queue = deque([root])
    while len(queue)!=0:
        current_node = queue.popleft()
        childrens = int(input(f"Enter how many childrens for {current_node.data}"))
        for i in range(childrens):
            data = int(input(f"Enter Data for child {i+1} of the {current_node.data}"))
            child_node = TreeNode(data)
            current_node.children.append(child_node)
            queue.append(child_node)
    return root

# root = take_input_level_wise()
# print(print_children_detailed(root))
