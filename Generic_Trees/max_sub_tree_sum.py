

from take_input import take_input_level_wise

def max_Subtree_sum(root):

    answer = {
        "sum":float("-inf"),
        "node":None
    }
    def subtree(node):
        if (node is None):
            return answer
        total = node.data
        for child in node.children:
            total = total + subtree(child)
        if total>answer["sum"]:
            answer["sum"] = total
            answer["node"] = node.data
        return total
    subtree(root)

    return answer["sum"], answer["node"]

root = take_input_level_wise()
print(max_Subtree_sum(root))

def max_subtree_sum(root):
    if root is None:
        return 0, float("-inf"), None

    current_sum = root.data
    best_sum = float("-inf")
    best_node = None

    for child in root.children:
        # Recurse: get the child's subtree sum and the best result found in its branch
        child_sum, child_best_sum, child_best_node = max_subtree_sum(child)
        # Add child's full subtree sum to the current node's sum
        current_sum += child_sum
        # Keep track of the best result found in the children
        if child_best_sum > best_sum:
            best_sum = child_best_sum
            best_node = child_best_node
    # Compare the current node's total subtree sum with the best found in children
    if current_sum >= best_sum:
        best_sum = current_sum
        best_node = root
    return current_sum, best_sum, best_node