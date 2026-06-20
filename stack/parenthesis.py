

from main_stack import StackUsingList

# def isValid(string):


#     stack = StackUsingList()

#     for ch in string:

#         if ch in "({[":

#             stack.push(ch)
        
#         else:

#             if stack.is_empty():

#                 return False

#             top = stack.top()

#             if ch==")" and top!="(":

#                 return False
            
#             if ch=="}" and top!="{":

#                 return False
            
            
#             if ch=="]" and top!="[":

#                 return False
        
#             stack.pop()
    
#     return stack.is_empty()


# print(isValid("()[]{}"))


def isValid( s):
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()

        return len(stack) == 0
        
