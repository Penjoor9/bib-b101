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
# stack
Stack=[]
input_str = "()(()"
for char in input_str:
    if char == "(":
        Stack.append(char)
    if char == ")":
        Stack.pop(char)

length=len(Stack)

if length !=0 :
    print("False")
else:
    print("True")
# stack
input_str = ")))"
stack = []
for char in input_str:
  if char == "(":
      stack.append(char)
      if char == ")":
       stack.pop()
length = len(stack)
if length == 0:
    print('True')
else:
    print("False")