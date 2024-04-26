input_str = "((())))(()(())())(()())))))((()())()))()()())())(())(()(())(())()(((()()(((((()(((()))()(()(())()))(((("
floor_index= 0

for i in input_str:
    if i== "(":
        floor_index= floor_index+1
    if i ==")":
        floor_index= floor_index-1
print('the final floor is',floor_index)
# problem 2
def is_valid_brackets(input_str):
    stack = []
    brackets = {'(': ')', ')': '('}
    for char in input_str:
        if char in brackets:
            if stack and brackets[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
    return not stack

# Example usage
input_str = "()(()"
print(is_valid_brackets(input_str))