

from implementation import BinaryTreeNode,print_binary_tree_node
from collections import deque

def take_input_level_wise():
    data = int(input("Enter data for the root node : "))
    root = BinaryTreeNode(data)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        left = int(input(f"Enter left data for {node.data} or -1 for ending: "))
        right = int(input(f"Enter right data for {node.data} or -1 for ending:  "))
        if left!=-1:
            node.left = BinaryTreeNode(left)
            queue.append(node.left)
        if right!=-1:
            node.right = BinaryTreeNode(right)
            queue.append(node.right)

    return root

# root = take_input_level_wise()
# print_binary_tree_node(root)


# def take_input():
#     data = int(input("Enter data for node or -1 to end:"))
#     if data==-1:
#         return None
    
#     node = BinaryTreeNode(data)
#     print(f"Enter left child data for {data}")
#     node.left = take_input()
#     print(f"Enter data for right child {data}")
#     node.right = take_input()
#     return node

# root = take_input()
# print_binary_tree_node(root)
