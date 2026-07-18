

from collections import deque
from Generic_Trees.take_input import take_input_level_wise
# def large_data_in_each_level(root):
#     data = []
#     data.append(root.data)
#     queue = deque([root])
#     while len(queue)!=0:
#         root = queue.popleft()
#         large = 0
#         for child in root.children:
#             if child.data>large:
#                 large = child.data
#             queue.append(child)
#         if len(root.children)!=0:
#          data.append(large)
#     return data
# root = take_input_level_wise()
# print(large_data_in_each_level(root))

def large_data_in_each_level(root):
    result = []
    if root is None:
        return []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        largest = float("-inf")
        for _ in range(level_size):
            node = queue.popleft()
            if node.data>largest:
                largest=node.data
            for child in node.children:
                queue.append(child)
        result.append(largest)
    return result
root = take_input_level_wise()
print(large_data_in_each_level(root))