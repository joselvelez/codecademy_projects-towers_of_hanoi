from node import Node

class Stack:
    def __init__(self, name):
        self.name = name
        self.top_node = None
        self.size = 0
        self.limit = 1000

    def peek(self):
        if self.is_empty():
            return "This stack is empty!"
        else:
            return self.top_node.get_value()

    def push(self, value):
        if self.has_space():
            node = Node(value)
            node.set_next_node(self.top_node)
            self.top_node = node
            self.size += 1
        else:
            return "Stack is full!"

    def pop(self):
        if self.is_empty():
            return "This stack is empty!"
        else:
            popped_node = self.top_node
            self.top_node = popped_node.get_next_node()
            self.size -= 1
            return popped_node

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.limit > self.size

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def print_items(self):
        pointer = self.top_node
        print_list = []
        while pointer:
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        print_list.reverse()
        print("{name} Stack: {stack}".format(name=self.get_name(), stack=print_list))

''' Test Code '''
# test_stack = Stack('test')
# test_stack.push(3)
# test_stack.push(2)
# test_stack.push(1)
# test_stack.push(40)
# new_stack = Stack('new')
# print(test_stack.peek())
# print(test_stack.is_empty())
# print(test_stack.has_space())
# print(test_stack.get_size())
# test_stack.print_items()
# new_stack.print_items()
# test_stack.pop()
# test_stack.print_items()