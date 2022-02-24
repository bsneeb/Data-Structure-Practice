''' Implementing a stack in python. Stacks are LIFO Data structures
    Functions:
        Push: Add to top
        Pop: remove from top
        Complexity: O(1)
    Applications:
        Reverse words
        Compilers
        Browsers
    '''


def create_stack():
    stack = []
    return stack


def stack_length(stack):
    return len(stack)


def push(stack, element):
    stack.append(element)


def pop(stack):
    if len(stack) == 0:
        return "stack is empty"

    return stack.pop()


if __name__ == '__main__':
    stack = create_stack()
    push(stack, 3)
    push(stack, 6)
    push(stack, 3)
    push(stack, 2)
    push(stack, 1)
    push(stack, 8)
    print(stack)
    stack.pop()
    print(stack)
