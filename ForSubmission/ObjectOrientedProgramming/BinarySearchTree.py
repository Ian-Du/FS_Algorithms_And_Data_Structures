class Node:
    def __init__(self, key, data):
        self.left_child = None
        self.right_child = None
        self.key = key
        self.data = data

    def insert_node(self, node):
        if node.key < self.key:
            if self.left_child is None:
                self.left_child = node
            else:
                self.left_child.insert_node(node)
        elif node.key >= self.key:
            if self.right_child is None:
                self.right_child = node
            else:
                self.right_child.insert_node(node)

    def get_node(self, key):
        if key < self.key:
            if self.left_child is None:
                return str(key) + " Not Found"
            return self.left_child.get_node(key)
        elif key > self.key:
            if self.right_child is None:
                return str(key) + " Not Found"
            return self.right_child.get_node(key)
        else:
            return self

    def __str__(self):
        return f"Key: {self.key}, Data: {self.data}"


tree = Node("Vahe", 40)
tree.insert_node(Node("Thomas", 45))
tree.insert_node(Node("Zeke", 123))
tree.insert_node(Node("Alex", 23))
tree.insert_node(Node("Ian", 66))

print(tree.get_node("Thomas"))
print(tree.get_node("Vahe"))
print(tree.get_node("Zeke"))
print(tree.get_node("Alex"))
print(tree.get_node("Al"))  # should return "Alex is not found"

