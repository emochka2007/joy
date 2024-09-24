import re
def polish_notation(m):
    """polish notation"""
    stack = []
    for token in m:
        if isinstance(token,int) or is_number(token):
            stack.append(token)
        elif isinstance(token, list):
            stack.append(token)
        else:
            perform_operation(token, stack) 
    return stack
def perform_operation(oper,stack):
    if oper == "first":
        stack.append(stack.pop()[0])
    if oper == "rest":
        stack_top = stack.pop()
        del stack_top[0]
        stack.append(stack_top)
    if oper == "cons":
        stack_top = stack.pop()
        stack_top.insert(0, stack.pop())
        stack.append(stack_top)
    if oper == "dup":
        stack.append(stack[-1])
    if oper == "drop":
        stack.pop()
    if oper == "swap":
        last = stack.pop()
        pre_last = stack.pop()
        stack.append(last)
        stack.append(pre_last)
    if oper == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    if oper == '-':
        a, b = stack.pop(), stack.pop()
        stack.append(b - a)
    if oper == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    if oper == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
        
def is_number(text):
    """checks if string is number"""
    if not isinstance(text, str):
        return False
    number_regex = r'^[0-9]+$'
    return re.match(number_regex, text) is not None

def tokenizer(text):
    """app_split"""
    splitted = []
    temp_str = ""
    for i in text:
       if i in ("[", "]"):
           if temp_str != "":
               splitted.append(temp_str)
           splitted.append(i)
           temp_str = ""
       elif i != " ":
           temp_str = f"{temp_str}{i}"
       else:
           if temp_str != "":
               splitted.append(temp_str)
           temp_str = ""
    splitted.append(temp_str)

    return splitted
# # "3 2 swap -" -> [3,2,"swap","-"]
# split_exp = "3      5 swap -"
# # first_exp = "[5 2 3] first" #1   
# first_exp = "[1 2]    3  4 5" #1   
# print(app_split(first_exp))
# # print(polish_notation(app_split(first_exp)))

# "[1 2]3 4 5" -> ["43, [","1","2","]","3","4","5"] -> [43,["1","2"],"3","4","5"]
def match_brackets(splitted):
    stack = []
    for i in splitted:
        if i != "]":
            if is_number(i):
                stack.append(int(i))
            else:
                stack.append(i)
        else:
            matched = []
            while stack[-1] != "[":
                matched.insert(0, stack.pop())
            stack.pop()
            stack.append(matched)         
    return stack

print(polish_notation(match_brackets(tokenizer("[1 2 3] first"))))
print(polish_notation(match_brackets(tokenizer("[1 2 3] rest"))))
print(polish_notation(match_brackets(tokenizer("42 [1 2 3] cons"))))
print(polish_notation(match_brackets(tokenizer("[1 2 3] dup first swap rest cons"))))
# [1 2 3] first -> 1
# [1 2 3] rest -> [2 3]
# 42 [1 2 3] cons -> [42 1 2 3]
# [1 2 3] dup first swap rest cons