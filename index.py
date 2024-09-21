import re
def polish_notation(m):
    """polish notation"""
    stack = []
    inner_arr = []
    for i, token in enumerate(m):
        if isinstance(token,int) or is_number(token):
            stack.append(int(token))
        elif isinstance(token, list):
            inner_arr = []
            for i in token:
                inner_arr.append(int(i))
        else:
            perform_operation(token, stack, inner_arr) 
    return stack
def perform_operation(token,stack, inner_arr):
    if token == "first":
        stack.append(inner_arr[0])
    if token == "dup":
        stack.append(stack[-1])
    if token == "drop":
        stack.pop()
    if token == "swap":
        last = stack.pop()
        pre_last = stack.pop()
        stack.append(last)
        stack.append(pre_last)
    if token == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    if token == '-':
        a, b = stack.pop(), stack.pop()
        stack.append(b - a)
    if token == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    if token == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
        
def is_number(text):
    """checks if string is number"""
    if not isinstance(text, str):
        return False
    number_regex = r'^[0-9]+$'
    return re.match(number_regex, text) is not None

def app_split(text):
    """app_split"""
    splitted = []
    bracket_open = False
    inner_array = []
    temp_str = ""
    for i in text:
       if i != " ":
           if i == "]":
               splitted.append(inner_array)
               bracket_open=False
           elif bracket_open:
               inner_array.append(i)
           elif i == "[":
               bracket_open=True
           else: 
               temp_str = f"{temp_str}{i}" 
       if i == " " and not bracket_open:
           if temp_str != "":
               splitted.append(temp_str)
           temp_str = ""
    splitted.append(temp_str)

    return splitted
# "3 2 swap -" -> [3,2,"swap","-"]
split_exp = "3 2 swap -"
first_exp = "[5 2 3] first" #1
print(polish_notation(app_split(split_exp)))
print(polish_notation(app_split(first_exp)))