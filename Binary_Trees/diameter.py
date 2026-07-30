

from take_input import take_input_level_wise

root = take_input_level_wise()

answer = [0]
def diameter_of_tree(root):
    
    if (root is None):
        return 0
    left_tree_height = diameter_of_tree(root.left)
    right_tree_height = diameter_of_tree(root.right)
    diameter = left_tree_height+right_tree_height
    if diameter>answer[0]:
        answer[0]=diameter
    return 1 + max(left_tree_height,right_tree_height)

height = diameter_of_tree(root)

print(f"Diameter {answer[0]} and height is {height} ")