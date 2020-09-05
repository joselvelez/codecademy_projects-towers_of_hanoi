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
        if self.is_empty():
            return "This stack is empty!"
        else:
            stack_list = []
            current_node = self.top_node
            while current_node:
                stack_list.append(current_node.get_value())
                current_node = current_node.get_next_node()
            print("{name} Stack: {stack}".format(name=self.get_name(), stack=stack_list))

''' Test Code '''
test_stack = Stack('test')
test_stack.push(10)
test_stack.push(20)
test_stack.push(30)
test_stack.push(40)

print(test_stack.peek())
print(test_stack.is_empty())
print(test_stack.has_space())
print(test_stack.get_size())
test_stack.print_items()
test_stack.pop()
test_stack.print_items()