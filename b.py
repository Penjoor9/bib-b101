input_str = "((())))(()(())())(()())))))((()())()))()()())())(())(()(())(())()(((()()(((((()(((()))()(()(())()))(((("
floor_index= 0

for i in input_str:
    if i== "(":
        floor_index= floor_index+1
    if i ==")":
        floor_index= floor_index-1
print('the final floor is',floor_index)