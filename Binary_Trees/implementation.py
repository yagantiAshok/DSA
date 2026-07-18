

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# root  = BinaryTreeNode(1)
# root.left = BinaryTreeNode(2)
# root.right = BinaryTreeNode(3)

def print_binary_tree_node(root):

    if (root is  None):
        return 
    print(root.data,end = " ")
    if (root.left is not None):
        print(f"Left->{root.left.data}",end=",")
    else:
        print(f"Left->{root.left}",end=",")

    if (root.right is not None):
        print(f"Right->{root.right.data}")
    else:
        print(f"Right->{root.right}")       

    print_binary_tree_node(root.left)
    print_binary_tree_node(root.right)

# print_binary_tree_node(root)



