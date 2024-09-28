import re
import operations
func_map = {}
def polish_notation(m):
    """polish notation"""
    stack = []
    while len(m) != 0:
        token = m[0]
        if isinstance(token,int) or is_number(token):
            stack.append(token)
            m.pop(0)
        elif isinstance(token, list):
            stack.append(token)
            m.pop(0)
        else:
            operations.perform_operation(token, stack, m, func_map) 
        print(f"M: {log_str(m)}")
        print(f"Stack: {log_str(stack)}")
        print("------------------------------")
        # input()
    return stack
def is_number(text):
    """checks if string is number"""
    if not isinstance(text, str):
        return False
    number_regex = r'^[0-9]+$'
    return re.match(number_regex, text) is not None

# todo to parser.py
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

# todo to parser.py
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
def log_str(m : list) -> str:
    string = ""
    for index, elem in enumerate(m):
        if not isinstance(elem, list):
            string += str(elem)
            if index != len(m) - 1:
                string += " "      
        else:
            string += "["
            string += log_str(elem)
            string += "] "
    return string

def to_power(a, n):
    if n == 0:
        return 1
    return a * to_power(a, n- 1)
# print(polish_notation(match_brackets(tokenizer("[fact dup  1 == [][dup 1 - fact *] if] def 5 fact"))))
# m = [dup 0 == [1][dup 1 - to_power *] if]
# stack = [4 4 4 4 * * *]
# [4 dup 3 == 0 [1][swap dup juggle swap 1 - to_power *] if ]
# [4 4 3 => 4 3 4 => 4 3 4 4 => 4 4 3 4 ]
# [4 4 4 4 * * * *]
print(polish_notation(match_brackets(tokenizer("[to_power dup 1 == [*][swap dup juggle swap 1 - to_power *] if] def 10 10 to_power")))) #64
