def perform_operation(oper: str,stack: [], m: [], func_map: {}):
    if oper == 'def':
        func = stack.pop()
        func_map[func[0]] = func[1:]
        m.pop(0)
    elif oper in {">", "<", "=="}:
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
        m.pop(0)
        false_branch, true_branch, result = stack.pop(), stack.pop(), stack.pop()
        m[:0] = true_branch if result else false_branch
    elif oper == "first":
        stack.append(stack.pop()[0])
        m.pop(0)
    elif oper == "rest":
        stack_top = stack.pop()
        stack_top.pop(0)
        stack.append(stack_top)
        m.pop(0)
    elif oper == "cons":
        stack_top = stack.pop()
        stack_top.insert(0, stack.pop())
        stack.append(stack_top)
        m.pop(0)
    elif oper == "dup":
        stack.append(stack[-1])
        m.pop(0)
    elif oper == "drop":
        stack.pop()
        m.pop(0)
    elif oper == "swap":
        last = stack.pop()
        pre_last = stack.pop()
        stack.append(last)
        stack.append(pre_last)
        m.pop(0)
    elif oper in ["+", "-", "*", "/"]:
        a, b = stack.pop(), stack.pop()
        math_oper = {
            "+": a + b,
            "-": b - a,
            "*": a * b,
            "/": b / a
        }
        stack.append(math_oper[oper])
        m.pop(0)
    elif oper == "juggle":
        last = stack.pop()
        stack.insert(-2, last) 
        m.pop(0)
    elif oper in func_map:
        m.pop(0)
        m[:0] = func_map[oper]
        