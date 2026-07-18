
from Generic_Trees.genric_trees import TreeNode,print_children_detailed
from collections import deque


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

