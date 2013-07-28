pointer = -1
stack = []

def push(value):
    global pointer
    """ Push to top of stack """
    stack.append(value)
    pointer += 1

def pop(index=hex(pointer)):
    # Pop the passed index of the stack, or pop the top value
    return stack[hextopointer(index)]
    
def hextopointer(value):
    """ Convert hex pointer for stack to array index """
    return int(value, 16)