

from take_input import take_input_level_wise
root = take_input_level_wise()

def  is_tree_balanced(root):
    if (root is None):
        return 0,True
    left_tree_height,is_left_tree_balanced = is_tree_balanced(root.left)
    right_tree_height,is_right_tree_balanced = is_tree_balanced(root.right)

    if (is_left_tree_balanced is False or is_right_tree_balanced is False):
        return 1+max(left_tree_height,right_tree_height),False
    if (abs(left_tree_height-right_tree_height))<=1:
        return 1+max(left_tree_height,right_tree_height),True
    return 1+max(left_tree_height,right_tree_height),False
# balanced = (left_tree_balanced and right_tree_balanced and abs(left_tree_height-right_tree_height))<=1)
# return  1+max(left_tree_height,right_tree_height),balanced
    
height,balanced = is_tree_balanced(root)
print(balanced)