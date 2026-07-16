

from take_input import take_input_level_wise

def count_nodes(root):
    if(root==None):
        return 0 
    numofnodes = 1
    for child in root.children:
        numofnodes = numofnodes + count_nodes(child)
    return numofnodes

root = take_input_level_wise()
print(count_nodes(root))
