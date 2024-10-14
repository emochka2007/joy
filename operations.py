def perform_operation(oper: str,stack: [], m: [], func_map: {}):
    if oper == 'def':
        check_if_enough_stack(stack, 1, oper)
        check_valid_types(stack, [list])
        func = stack.pop()
        func_map[func[0]] = func[1:]
        m.pop(0)
    elif oper in {">", "<", "=="}:
        check_if_enough_stack(stack, 2, oper)
        check_valid_types(stack, [int, int])
        last = stack.pop()
        pre_last = stack.pop()
        math_oper = {
            ">": pre_last > last,
            "==": pre_last == last,
            "<": pre_last < last
        }
        stack.append(math_oper[oper])
        m.pop(0)
    elif oper == "if":
        check_if_enough_stack(stack, 2, oper)
        check_valid_types(stack, [list, list])
        m.pop(0)
        false_branch, true_branch, result = stack.pop(), stack.pop(), stack.pop()
        m[:0] = true_branch if result else false_branch
    elif oper == "first":
        check_if_enough_stack(stack, 1, oper)
        check_valid_types(stack, [list])
        stack_top = stack.pop()
        if len(stack_top) < 1:
             print(f"Not enough elements inside array for first operation. Stack: {stack}")
             exit(1)
        stack.append(stack_top[0])
        m.pop(0)
    elif oper == "rest":
        check_if_enough_stack(stack, 1, oper)
        check_valid_types(stack, [list])
        stack_top = stack.pop()
        if len(stack_top) < 1:
             print(f"Not enough elements inside array for rest operation. Stack: {stack}")
             exit(1)
        sliced_stack = stack_top[1:]
        stack.append(sliced_stack)
        m.pop(0)
    elif oper == "cons":
        check_if_enough_stack(stack, 2, oper)
        check_valid_types(stack, [list, int])
        stack_top = stack.pop()
        sliced_stack = [stack.pop()] + stack_top
        stack.append(sliced_stack)
        m.pop(0)
    # no type check needed
    elif oper == "dup":
        check_if_enough_stack(stack, 1, oper)
        stack.append(stack[-1])
        m.pop(0)
    # no type check needed
    elif oper == "drop":
        check_if_enough_stack(stack,1, oper)
        stack.pop()
        m.pop(0)
    # no type check needed
    elif oper == "swap":
        check_if_enough_stack(stack, 2, oper)
        last = stack.pop()
        pre_last = stack.pop()
        stack.append(last)
        stack.append(pre_last)
        m.pop(0)
    elif oper in ["+", "-", "*", "/"]:
        check_if_enough_stack(stack, 2, oper)
        check_valid_types(stack, [int, int])
        a, b = stack.pop(), stack.pop()
        math_oper = {
            "+": a + b,
            "-": b - a,
            "*": a * b,
            "/": b / a
        }
        stack.append(math_oper[oper])
        m.pop(0)
    elif oper == "rot":
        check_if_enough_stack(stack, 3, oper)
        last = stack.pop()
        stack.insert(-2, last) 
        m.pop(0)
    elif oper == "null":
        check_if_enough_stack(stack, 1, oper)
        check_valid_types(stack, [list])
        last = stack.pop()
        stack.append(len(last) == 0)
        m.pop(0)
    elif oper == "stop":
        print("Stop oper")
        exit(1)
    elif oper == "dip":
        m.pop(0)
        action = stack.pop()
        last = stack.pop()
        m.insert(0, last)
        m[:0] = action
    elif oper == "rolldown": # eq to rot rot
        # X Y Z -> Y Z X moves y and z down, moves x up
        m.pop(0)
        z = stack.pop()
        y = stack.pop()
        x = stack.pop()
        stack.append(y)
        stack.append(z)
        stack.append(x)
    elif oper == 'i':
        m.pop(0)
        l = stack.pop()
        # check_valid_types(stack, [list])
        m[:0] = l
    elif oper in func_map:
        m.pop(0)
        m[:0] = func_map[oper]
    else:
        print(func_map)
        print(f"No operation found: {oper} {repr(oper)}")
        exit(1)
        
def check_if_enough_stack(stack:[], required: int, operation: str):
    if len(stack) < required:
        print(f"Not enough elements on stack for operation {operation}. \n Stack: {stack}")
        exit(1)

# 12 1 [1 2 3]
def check_valid_types(stack:[], types_array: [type]):
    # iterable
    for i, elem in enumerate(types_array):
        if len(stack) == 0:
            print("Stack len equal zero")
            exit(1)
        stack_type = type(stack[len(stack) - 1 - i])
        if stack_type != elem:
            print(f"Incorrect type on stack, expected {elem}, received {stack_type}") 
            exit(1)