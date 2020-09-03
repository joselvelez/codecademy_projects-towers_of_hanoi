class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

''' Debug / Test Statements '''
# node1 = Node(10)
# node2 = Node(20)
# node1.set_next_node(node2)
# print(node1.get_next_node())
# print(node2)